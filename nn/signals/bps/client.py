"""
BPS Web API client.

Wraps the BPS Statistics Indonesia Web API (https://webapi.bps.go.id).
List methods return ``list[dict]`` so results are usable without pandas.
Call ``to_df()`` to convert any result to a DataFrame.

Example
-------
>>> client = BPSWebApiClient(token="...")
>>> domains = client.list_domain()
>>> to_df(domains)
"""

from __future__ import annotations

import logging
import os
import pandas as pd
import requests
from tqdm import tqdm
from typing import Callable

BASE_URL = "https://webapi.bps.go.id/v1/api"

# Indonesian month name → month number. "Tahunan" is handled separately in
# normalize_date (explicit branch, not a map entry) so it is kept as YYYY-01-01
# but remains distinguishable from Januari via the turtahun column.
_MONTH_MAP: dict[str, int] = {
    "januari": 1,
    "februari": 2,
    "maret": 3,
    "april": 4,
    "mei": 5,
    "juni": 6,
    "juli": 7,
    "agustus": 8,
    "september": 9,
    "oktober": 10,
    "november": 11,
    "desember": 12,
}

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
log = logging.getLogger(__name__)
log.setLevel(os.getenv("LOG_LEVEL", "INFO").upper())


# A processor takes the raw API response dict and the variable ID string,
# and returns a DataFrame shaped however the caller needs it.
DataProcessor = Callable[[dict, str], pd.DataFrame]


def _parse_response(
    res: dict, var: str
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame | None, dict]:
    """Parse the common structure of a dynamic data API response.

    Extracts the four building blocks shared by every processor:

    - ``vervar_df``  — vertical variables (rows dimension, e.g. provinces)
    - ``turvar_df``  — derived variables (column dimension, e.g. PLN / non-PLN)
    - ``turtahun_df``— derived periods (sub-annual breakdown); ``None`` when absent
    - ``datacontent``— flat dict mapping composite key → numeric value

    The composite key format is::

        {vervar_id}{var_id}{turvar_id}{tahun_id}{turth_id}

    All IDs are concatenated as plain strings with no separator, so the
    mapping is only unambiguous when you already know the component values.

    Parameters
    ----------
    res:
        Raw JSON response from the ``/api/list?model=data`` endpoint.
    var:
        Variable ID passed to the original request; needed when building keys.

    Returns
    -------
    Tuple of ``(vervar_df, turvar_df, turtahun_df, datacontent)``.
    """
    vervar_df = pd.DataFrame(
        [[x["val"], x["label"]] for x in res["vervar"]],
        columns=["id_var", "variable"],
    ).sort_values("id_var", ignore_index=True)

    turvar_df = pd.DataFrame(
        [[x["val"], x["label"]] for x in res["turvar"]],
        columns=["id_tur_var", "turvar"],
    ).sort_values("id_tur_var", ignore_index=True)

    # turtahun is optional — only present for sub-annual (e.g. monthly) variables
    turtahun_df = None
    if "turtahun" in res:
        turtahun_df = pd.DataFrame(
            [[x["val"], x["label"]] for x in res["turtahun"]],
            columns=["id_tur_th", "turtahun"],
        ).sort_values("id_tur_th", ignore_index=True)

    datacontent: dict = res["datacontent"]

    return vervar_df, turvar_df, turtahun_df, datacontent


def _build_keys(
    rows: pd.DataFrame, var: str, tahun_val: str, turtahun_df: pd.DataFrame | None
) -> pd.Series:
    """Build composite datacontent lookup keys for every row in *rows*.

    Concatenates the component IDs in the order the API expects::

        {vervar_id}{var_id}{turvar_id}{tahun_id}[{turth_id}]

    Using vectorised string ops on a Series instead of looping makes this
    O(n) and avoids the per-row overhead of ``iterrows``.

    Parameters
    ----------
    rows:
        DataFrame containing at least ``id_var``, ``id_tur_var``, and
        optionally ``id_tur_th`` columns.
    var:
        Variable ID (scalar string, same for every row).
    tahun_val:
        Period ID for this particular year column.
    turtahun_df:
        Present when the variable has sub-annual breakdowns; ``None`` otherwise.

    Returns
    -------
    :class:`pandas.Series` of composite key strings, one per row.
    """
    keys = (
        rows["id_var"].astype(str)
        + str(var)
        + rows["id_tur_var"].astype(str)
        + str(tahun_val)
        # append derived-period ID only when the variable has sub-annual data
        + (rows["id_tur_th"].astype(str) if turtahun_df is not None else "")
    )
    return keys


def wide(res: dict, var: str) -> pd.DataFrame:
    """Process a dynamic data response into a **wide** (pivoted) DataFrame.

    Each unique combination of vertical variable and derived variable becomes
    one row. Each requested year becomes one column. This mirrors the layout
    shown on the BPS website.

    Example output::

        variable   | turvar | 2000  | 2001
        INDONESIA  | Listrik PLN      | 83.68 | 85.20
        INDONESIA  | Non-PLN          | 16.32 | 14.80

    Parameters
    ----------
    res:
        Raw JSON response from ``/api/list?model=data``.
    var:
        Variable ID from the original request.

    Returns
    -------
    Wide :class:`pandas.DataFrame` with years as columns.
    """
    vervar_df, turvar_df, turtahun_df, datacontent = _parse_response(res, var)

    # cross-join so every (vervar × turvar) combination gets its own row
    result = vervar_df.merge(turvar_df, how="cross")
    if turtahun_df is not None:
        result = result.merge(turtahun_df, how="cross")

    tahun_df = pd.DataFrame(
        [[x["val"], x["label"]] for x in res["tahun"]],
        columns=["val", "label"],
    ).sort_values("val", ignore_index=True)

    # add one column per year; values come from an O(1) dict lookup per cell
    for _, year_row in tahun_df.iterrows():
        keys = _build_keys(result, var, year_row["val"], turtahun_df)
        result[year_row["label"]] = keys.map(datacontent)

    return result


def long(res: dict, var: str) -> pd.DataFrame:
    """Process a dynamic data response into a **long** (tidy) DataFrame.

    Every data point becomes exactly one row with explicit columns for the
    variable labels, year, and value. This is the normalised form that is
    easiest to filter, aggregate, and join with other datasets.

    Example output::

        variable   | turvar | year | value
        INDONESIA  | Listrik PLN      | 2000 | 83.68
        INDONESIA  | Listrik PLN      | 2001 | 85.20
        INDONESIA  | Non-PLN          | 2000 | 16.32

    Parameters
    ----------
    res:
        Raw JSON response from ``/api/list?model=data``.
    var:
        Variable ID from the original request.

    Returns
    -------
    Long :class:`pandas.DataFrame` with columns
    ``variable``, ``turvar``, ``year``, ``value``.
    """
    vervar_df, turvar_df, turtahun_df, datacontent = _parse_response(res, var)

    # cross-join all dimension combinations, same as wide()
    rows = vervar_df.merge(turvar_df, how="cross")
    if turtahun_df is not None:
        rows = rows.merge(turtahun_df, how="cross")

    tahun_df = pd.DataFrame(
        [[x["val"], x["label"]] for x in res["tahun"]],
        columns=["val", "label"],
    ).sort_values("val", ignore_index=True)

    records = []
    for _, year_row in tahun_df.iterrows():
        keys = _build_keys(rows, var, year_row["val"], turtahun_df)
        # map each composite key to its value; unmapped keys become NaN
        values = keys.map(datacontent)

        # build one tidy record per (dimension combination × year)
        frame = rows[["variable", "turvar"]].copy()
        if turtahun_df is not None:
            frame["turtahun"] = rows["turtahun"]
        frame["year"] = year_row["label"]
        frame["value"] = values.values
        records.append(frame)

    return pd.concat(records, ignore_index=True)


def to_df(data: list[dict]) -> pd.DataFrame:
    """Convert a list of dicts (as returned by any ``list_*`` method) to a DataFrame.

    Parameters
    ----------
    data:
        Output of any ``list_*`` method on :class:`BPSWebApiClient`.

    Returns
    -------
    :class:`pandas.DataFrame`
    """
    return pd.DataFrame(data)


def normalize_date(
    df: pd.DataFrame,
    year_col: str = "year",
    period_col: str = "turtahun",
) -> pd.DataFrame:
    """Add a ``ds`` column (``YYYY-MM-DD``) to a long-format DataFrame.

    Follows the Airflow ``ds`` convention: a date string representing the
    first day of the observation period.

    * Monthly rows (``turtahun`` = Indonesian month name) → ``YYYY-MM-01``.
    * Annual aggregate rows (``turtahun == "Tahunan"``) → ``YYYY-01-01``
      (start-of-year anchor; distinguish from Januari via the ``turtahun``
      column — they are *not* the same observation).
    * Annual-only data (no ``turtahun`` column) → ``YYYY-01-01``.

    Parameters
    ----------
    df:
        Long-format DataFrame as returned by :func:`long`.
    year_col:
        Name of the column containing the year value (default ``"year"``).
    period_col:
        Name of the column containing the Indonesian period label
        (default ``"turtahun"``). Ignored when the column is absent.

    Returns
    -------
    Copy of *df* with a new ``ds`` column of type ``str`` (``YYYY-MM-DD``).
    Rows whose period label cannot be resolved are assigned ``NaT``.

    Example
    -------
    >>> df = client.get_data(domain="0000", var="1890", th="120")
    >>> normalize_date(df).head()
       variable  ...  year          ds
    0  INDONESIA ...  2020  2020-01-01
    1  INDONESIA ...  2020  2020-02-01
    """
    df = df.copy()

    if period_col in df.columns:
        lower = df[period_col].str.lower()
        # Monthly rows: look up the Indonesian month name
        month_num = lower.map(_MONTH_MAP)
        # Annual aggregate rows: explicitly anchor to month 1 (start of year).
        # Not in _MONTH_MAP because "Tahunan" ≠ "Januari" semantically —
        # use turtahun to distinguish them after the fact.
        month_num = month_num.where(lower != "tahunan", other=1)
    else:
        # annual-only data — every row is January
        month_num = pd.Series(1, index=df.index)

    # combine year + month into a Timestamp then format as YYYY-MM-DD
    df["ds"] = pd.to_datetime(
        df[year_col].astype(str)
        + "-"
        + month_num.astype("Int64").astype(str).str.zfill(2)
        + "-01",
        format="%Y-%m-%d",
        errors="coerce",
    ).dt.strftime("%Y-%m-%d")

    return df


class BPSWebApiClient:
    """Client for the BPS Statistics Indonesia Web API.

    Parameters
    ----------
    token:
        API token obtained from https://webapi.bps.go.id/developer/
    """

    def __init__(self, token: str) -> None:
        self.token = token
        self._session = requests.Session()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _get(self, endpoint: str, params: dict | None = None) -> dict:
        """Send a GET request and return the parsed JSON response.

        Automatically injects the API key into every request. Raises
        ``requests.HTTPError`` on non-2xx responses and ``ValueError``
        when the API returns a non-OK status in the payload.
        """
        p = {"key": self.token}
        if params:
            p.update(params)
        log.debug("GET %s %s", endpoint, p)
        res = self._session.get(f"{BASE_URL}/{endpoint}", params=p)
        res.raise_for_status()
        data = res.json()
        if data.get("status") != "OK":
            raise ValueError(data.get("message", "API returned non-OK status"))
        return data

    def _paginate(
        self, model: str, domain: str, fields: list[str], **params
    ) -> list[dict]:
        """Fetch all pages for a list endpoint and return a flat list of dicts.

        Parameters
        ----------
        model:
            Value of the ``model`` query parameter (e.g. ``"subject"``).
        domain:
            Four-digit BPS domain ID.
        fields:
            Keys to extract from each item in the response.
        **params:
            Additional query parameters forwarded to the API.
        """
        base_params = {
            "model": model,
            "domain": domain,
            "lang": "ind",
            "page": 1,
            **params,
        }
        res = self._get("list", base_params)

        if res.get("data") == "" or not res.get("data"):
            return []

        rows: list[dict] = [{f: item.get(f) for f in fields} for item in res["data"][1]]
        total_pages = res["data"][0]["pages"]
        log.debug("model=%s domain=%s total_pages=%d", model, domain, total_pages)

        for page in tqdm(range(2, total_pages + 1), desc=model, leave=False):
            res = self._get("list", {**base_params, "page": page})
            if res.get("data") == "" or not res.get("data"):
                break
            rows.extend({f: item.get(f) for f in fields} for item in res["data"][1])

        return rows

    # ------------------------------------------------------------------
    # Domain
    # ------------------------------------------------------------------

    def list_domain(self, type: str = "all", prov: str | None = None) -> list[dict]:
        """Return all BPS domain websites.

        Parameters
        ----------
        type:
            Domain type filter. One of:

            - ``"all"`` – every domain (national, province, city/regency)
            - ``"prov"`` – province domains only
            - ``"kab"`` – city/regency domains only
            - ``"kabbyprov"`` – all city/regency domains within a province
              (requires ``prov``)
        prov:
            Province domain ID (four digits). Required when ``type="kabbyprov"``.

        Returns
        -------
        List of dicts with keys: ``domain_id``, ``domain_name``, ``domain_url``, ``level``.
        """
        params: dict = {"type": type}
        if prov:
            params["prov"] = prov

        res = self._get("domain", params)

        level_map = {"0000": "nasional"}
        rows = []
        for item in res["data"][1]:
            did = item["domain_id"]
            if did == "0000":
                level = "nasional"
            elif did.endswith("00"):
                level = "provinsi"
            else:
                level = "kota/kabupaten"
            rows.append(
                {
                    "domain_id": did,
                    "domain_name": item["domain_name"],
                    "domain_url": item["domain_url"],
                    "level": level,
                }
            )

        return rows

    # ------------------------------------------------------------------
    # Subject
    # ------------------------------------------------------------------

    def list_subject(
        self,
        domain: str = "0000",
        subcat: str | None = None,
        lang: str = "ind",
    ) -> list[dict]:
        """Return all subjects for a domain.

        Parameters
        ----------
        domain:
            Four-digit BPS domain ID. Defaults to ``"0000"`` (national).
        subcat:
            Subject category ID to filter by. When omitted, all subjects
            across every category are returned.
        lang:
            Response language. One of ``"ind"`` (Indonesian) or ``"eng"`` (English).

        Returns
        -------
        List of dicts with keys: ``sub_id``, ``title``, ``subcat_id``, ``subcat``, ``ntabel``.
        """
        params: dict = {"lang": lang}
        if subcat:
            params["subcat"] = subcat
        fields = ["sub_id", "title", "subcat_id", "subcat", "ntabel"]
        return self._paginate("subject", domain, fields, **params)

    # ------------------------------------------------------------------
    # Subject Categories
    # ------------------------------------------------------------------

    def list_subject_categories(
        self,
        domain: str = "0000",
        lang: str = "ind",
    ) -> list[dict]:
        """Return all subject categories for a domain.

        Parameters
        ----------
        domain:
            Four-digit BPS domain ID. Defaults to ``"0000"`` (national).
        lang:
            Response language. One of ``"ind"`` (Indonesian) or ``"eng"`` (English).

        Returns
        -------
        List of dicts with keys: ``subcat_id``, ``title``.
        """
        fields = ["subcat_id", "title"]
        return self._paginate("subcat", domain, fields, lang=lang)

    # ------------------------------------------------------------------
    # Dynamic Data
    # ------------------------------------------------------------------

    def list_variable(
        self,
        domain: str = "0000",
        subject: str | None = None,
        lang: str = "ind",
    ) -> list[dict]:
        """Return all variables (dynamic table indicators) for a domain.

        Parameters
        ----------
        domain:
            Four-digit BPS domain ID. Defaults to ``"0000"`` (national).
        subject:
            Subject ID to filter variables by. When omitted, all variables
            are returned.
        lang:
            Response language. One of ``"ind"`` or ``"eng"``.

        Returns
        -------
        List of dicts with keys: ``var_id``, ``title``, ``sub_id``, ``sub_name``,
        ``def``, ``notes``, ``vertical``, ``unit``, ``graph_id``, ``graph_name``.
        """
        params: dict = {"lang": lang}
        if subject:
            params["subject"] = subject
        fields = [
            "var_id",
            "title",
            "sub_id",
            "sub_name",
            "def",
            "notes",
            "vertical",
            "unit",
            "graph_id",
            "graph_name",
        ]
        return self._paginate("var", domain, fields, **params)

    def list_period(
        self,
        domain: str = "0000",
        var: str | None = None,
        lang: str = "ind",
    ) -> list[dict]:
        """Return available period IDs for a variable.

        Parameters
        ----------
        domain:
            Four-digit BPS domain ID. Defaults to ``"0000"`` (national).
        var:
            Variable ID to filter periods by. When omitted, all periods
            across all variables are returned.
        lang:
            Response language. One of ``"ind"`` or ``"eng"``.

        Returns
        -------
        List of dicts with keys: ``th_id``, ``th``.
        """
        params: dict = {"lang": lang}
        if var:
            params["var"] = var
        fields = ["th_id", "th"]
        return self._paginate("th", domain, fields, **params)

    def list_derived_variable(
        self,
        domain: str = "0000",
        var: str | None = None,
        lang: str = "ind",
    ) -> list[dict]:
        """Return derived variables (column breakdowns) for a variable.

        Parameters
        ----------
        domain:
            Four-digit BPS domain ID. Defaults to ``"0000"`` (national).
        var:
            Variable ID to filter derived variables by.
        lang:
            Response language. One of ``"ind"`` or ``"eng"``.

        Returns
        -------
        List of dicts with keys: ``turvar_id``, ``turvar``, ``group_turvar_id``,
        ``name_group_turvar``.
        """
        params: dict = {"lang": lang}
        if var:
            params["var"] = var
        fields = ["turvar_id", "turvar", "group_turvar_id", "name_group_turvar"]
        return self._paginate("turvar", domain, fields, **params)

    def list_derived_period(
        self,
        domain: str = "0000",
        var: str | None = None,
        lang: str = "ind",
    ) -> list[dict]:
        """Return derived period data (sub-annual breakdowns) for a variable.

        Parameters
        ----------
        domain:
            Four-digit BPS domain ID. Defaults to ``"0000"`` (national).
        var:
            Variable ID to filter derived periods by.
        lang:
            Response language. One of ``"ind"`` or ``"eng"``.

        Returns
        -------
        List of dicts with keys: ``turth_id``, ``turth``, ``group_turth_id``,
        ``name_group_turth``.
        """
        params: dict = {"lang": lang}
        if var:
            params["var"] = var
        fields = ["turth_id", "turth", "group_turth_id", "name_group_turth"]
        return self._paginate("turth", domain, fields, **params)

    def get_data(
        self,
        domain: str,
        var: str,
        th: str,
        turvar: str | None = None,
        vervar: str | None = None,
        turth: str | None = None,
        lang: str = "ind",
        processor: DataProcessor = long,
    ) -> pd.DataFrame:
        """Fetch dynamic table data from the API and process it into a DataFrame.

        The API returns ``datacontent`` — a flat dict whose keys are composite
        ID strings of the form ``{vervar_id}{var_id}{turvar_id}{tahun_id}{turth_id}``.
        A *processor* function is responsible for turning that raw response into
        whatever shape is most useful.

        Parameters
        ----------
        domain:
            Four-digit BPS domain ID.
        var:
            Variable ID.
        th:
            Period ID. Accepts a single value (``"117"``), semicolon-separated
            values (``"116;117"``), or a range (``"115:117"``).
        turvar:
            Derived variable ID to filter columns.
        vervar:
            Vertical variable ID to filter rows.
        turth:
            Derived period ID (e.g. for monthly breakdowns).
        lang:
            Response language. One of ``"ind"`` or ``"eng"``.
        processor:
            Callable ``(res: dict, var: str) -> pd.DataFrame`` that shapes the
            raw API response. Defaults to :func:`long`. Pass :func:`wide` for
            the traditional pivoted layout, or any custom function.

        Returns
        -------
        :class:`pandas.DataFrame` whose shape depends on the chosen processor.
        """
        params: dict = {
            "model": "data",
            "domain": domain,
            "var": var,
            "th": th,
            "lang": lang,
        }
        log.debug("get_data initiate")

        if turvar:
            params["turvar"] = turvar
        if vervar:
            params["vervar"] = vervar
        if turth:
            params["turth"] = turth

        log.debug("get_data call API %s", params)
        res = self._get("list", params)

        log.info("get_data processing with %s", processor.__name__)
        result = processor(res, var)
        log.info("get_data done")

        return result
