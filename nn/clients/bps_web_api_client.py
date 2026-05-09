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
import pandas as pd
import requests
from tqdm import tqdm

BASE_URL = "https://webapi.bps.go.id/v1/api"

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
log = logging.getLogger(__name__)


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
        log.info("GET %s %s", endpoint, p)
        res = self._session.get(f"{BASE_URL}/{endpoint}", params=p)
        res.raise_for_status()
        data = res.json()
        if data.get("status") != "OK":
            raise ValueError(data.get("message", "API returned non-OK status"))
        return data

    def _paginate(self, model: str, domain: str, fields: list[str], **params) -> list[dict]:
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
        base_params = {"model": model, "domain": domain, "lang": "ind", "page": 1, **params}
        res = self._get("list", base_params)

        if res.get("data") == "" or not res.get("data"):
            return []

        rows: list[dict] = [{f: item.get(f) for f in fields} for item in res["data"][1]]
        total_pages = res["data"][0]["pages"]
        log.info("model=%s domain=%s total_pages=%d", model, domain, total_pages)

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
            rows.append({
                "domain_id": did,
                "domain_name": item["domain_name"],
                "domain_url": item["domain_url"],
                "level": level,
            })

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
        fields = ["var_id", "title", "sub_id", "sub_name", "def", "notes",
                  "vertical", "unit", "graph_id", "graph_name"]
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
    ) -> pd.DataFrame:
        """Return dynamic table data as a pivoted DataFrame.

        The API returns raw cell values keyed by a composite string
        ``{vervar_val}{var_id}{turvar_val}{tahun_val}{turth_val}``. This method
        reconstructs them into a human-readable table with vertical variables as
        rows and years as columns.

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

        Returns
        -------
        :class:`pandas.DataFrame` with vertical variables and derived variables
        as rows and years as columns containing the data values.
        """
        params: dict = {"model": "data", "domain": domain, "var": var, "th": th, "lang": lang}
        log.info("get_data %s", 'initiate')

        if turvar:
            log.info("get_data turvar %s", turvar)
            params["turvar"] = turvar
        if vervar:
            log.info("get_data vervar %s", vervar)
            params["vervar"] = vervar
        if turth:
            log.info("get_data turth %s", turth)
            params["turth"] = turth

        log.info("get_data call API started %s", params)
        res = self._get("list", params)
        log.info("get_data call API finished")

        log.info("get_data generate datacontent")
        datacontent = pd.DataFrame(
            {"key": res["datacontent"].keys(), "value": res["datacontent"].values()}
        ).sort_values("key", ignore_index=True)

        log.info("get_data generate vervar_df")
        vervar_df = pd.DataFrame(
            [[x["val"], x["label"]] for x in res["vervar"]],
            columns=["id_var", "variable"],
        ).sort_values("id_var", ignore_index=True)

        log.info("get_data generate turvar_df")
        turvar_df = pd.DataFrame(
            [[x["val"], x["label"]] for x in res["turvar"]],
            columns=["id_tur_var", "turunan variable"],
        ).sort_values("id_tur_var", ignore_index=True)

        result = vervar_df.merge(turvar_df, how="cross")

        log.info("get_data generate turtahun_df")
        turtahun_df = None
        if "turtahun" in res:
            turtahun_df = pd.DataFrame(
                [[x["val"], x["label"]] for x in res["turtahun"]],
                columns=["id_tur_th", "turunan tahun"],
            ).sort_values("id_tur_th", ignore_index=True)
            result = result.merge(turtahun_df, how="cross")

        tahun_df = pd.DataFrame(
            [[x["val"], x["label"]] for x in res["tahun"]],
            columns=["val", "label"],
        ).sort_values("val", ignore_index=True)

        log.info("get_data tahun_df.iterrows")
        for _, year_row in tahun_df.iterrows():
            result[year_row["label"]] = ""
            for i, row in result.iterrows():
                key = (
                    str(row["id_var"])
                    + str(var)
                    + str(row["id_tur_var"])
                    + str(year_row["val"])
                    + (str(row["id_tur_th"]) if turtahun_df is not None else "")
                )
                match = datacontent.loc[datacontent["key"].str.match(f"^{key}"), "value"]
                if not match.empty:
                    result.at[i, year_row["label"]] = match.iloc[0]
        log.info("get_data done")

        return result
