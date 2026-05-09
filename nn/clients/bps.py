import html
import io
from io import StringIO

import pandas as pd
import requests
from tqdm import tqdm

BASE_URL = "https://webapi.bps.go.id/v1/api"


class BPSWebApiClient:
    def __init__(self, token: str):
        """
        Initialize client object
        :param token: token from webapi website
        """
        self.token = token
        self._session = requests.Session()

    def _get(self, endpoint: str, params: dict | None = None) -> dict:
        p = {"key": self.token}
        if params:
            p.update(params)
        res = self._session.get(f"{BASE_URL}/{endpoint}", params=p)
        res.raise_for_status()
        data = res.json()
        if data.get("status") != "OK":
            raise ValueError(data.get("message", "API error"))
        return data

    def _list_pages(self, model: str, domain: str, page: int = 1, **kwargs) -> dict:
        params = {
            "model": model,
            "lang": "ind",
            "domain": domain,
            "page": page,
            "perpage": 100000,
            "keyword": "",
        }
        for k in ("month", "year", "var", "th", "turvar", "vervar", "turth"):
            if kwargs.get(k):
                params[k] = kwargs[k]
        return self._get("list", params)

    def _fetch_cached(self, key: str, domain: list | None) -> pd.DataFrame:
        content = self._session.get(_CACHE_URLS[key]).content
        df = pd.read_csv(
            io.StringIO(content.decode("utf-8")),
            sep="|",
            dtype={"domain": str},
            index_col=0 if key in ("pressrelease", "publication") else None,
        )
        if domain:
            df = df[df["domain"].isin(domain)]
        return df

    def _paginate(self, model: str, domain: str, fields: list[str], **kwargs) -> pd.DataFrame:
        rows = []
        res = self._list_pages(model, domain, **kwargs)
        if res["data"] == "":
            return pd.DataFrame(columns=fields)
        for item in res["data"][1]:
            rows.append({f: item.get(f) for f in fields})
        pages = res["data"][0]["pages"]
        for page in tqdm(range(2, pages + 1)):
            res = self._list_pages(model, domain, page=page, **kwargs)
            if res["data"] == "":
                break
            for item in res["data"][1]:
                rows.append({f: item.get(f) for f in fields})
        return pd.DataFrame(rows)

    def list_domain(self) -> pd.DataFrame:
        res = self._get("domain", {"type": "all"})
        rows = [
            {
                "domain_id": item["domain_id"],
                "domain_name": item["domain_name"],
                "domain_url": item["domain_url"],
            }
            for item in res["data"][1]
        ]
        df = pd.DataFrame(rows)
        df["level"] = "kota/kabupaten"
        df.loc[df["domain_id"].str.match(r"^.*00$"), "level"] = "provinsi"
        df.loc[df["domain_id"] == "0000", "level"] = "nasional"
        return df

    def list_dynamictable(self, domain: list | None = None, latest: bool = False) -> pd.DataFrame:
        if not latest:
            return self._fetch_cached("dynamictable", domain)
        domains = domain or self.list_domain()["domain_id"].tolist()
        fields = ["var_id", "title", "sub_id", "sub_name", "subcsa_id", "subcsa_name",
                  "def", "notes", "vertical", "unit", "graph_id", "graph_name"]
        frames = []
        for d in domains:
            df = self._paginate("var", d, fields)
            df["domain"] = d
            frames.append(df)
        return pd.concat(frames, ignore_index=True)

    def list_statictable(self, domain: list | None = None, latest: bool = False) -> pd.DataFrame:
        if not latest:
            return self._fetch_cached("statictable", domain)
        domains = domain or self.list_domain()["domain_id"].tolist()
        fields = ["table_id", "title", "subj_id", "subj", "updt_date", "size", "excel"]
        frames = []
        for d in domains:
            df = self._paginate("statictable", d, fields)
            df["domain"] = d
            frames.append(df)
        return pd.concat(frames, ignore_index=True)

    def list_pressrelease(
        self, domain: list | None = None, month: str = "", year: str = "", latest: bool = False
    ) -> pd.DataFrame:
        if not latest:
            df = self._fetch_cached("pressrelease", domain)
            if month and year:
                df = df[df["rl_date"].str.contains(f"{year}-{int(month):02d}")]
            return df
        domains = domain or self.list_domain()["domain_id"].tolist()
        fields = ["brs_id", "subj_id", "subj", "title", "abstract",
                  "rl_date", "updt_date", "pdf", "size", "slide", "thumbnail"]
        frames = []
        for d in domains:
            df = self._paginate("pressrelease", d, fields, month=month, year=year)
            df["domain"] = d
            frames.append(df)
        return pd.concat(frames, ignore_index=True)

    def list_publication(
        self, domain: list | None = None, month: str = "", year: str = "", latest: bool = False
    ) -> pd.DataFrame:
        if not latest:
            df = self._fetch_cached("publication", domain)
            if month and year:
                df = df[df["rl_date"].str.contains(f"{year}-{int(month):02d}")]
            return df
        domains = domain or self.list_domain()["domain_id"].tolist()
        fields = ["pub_id", "title", "abstract", "issn", "sch_date",
                  "rl_date", "updt_date", "cover", "pdf", "size"]
        frames = []
        for d in domains:
            df = self._paginate("publication", d, fields, month=month, year=year)
            df["domain"] = d
            frames.append(df)
        return pd.concat(frames, ignore_index=True)

    def view_statictable(self, domain: str, table_id: str, lang: str = "ind") -> pd.DataFrame:
        res = self._get("view", {"model": "statictable", "lang": lang, "domain": domain, "id": table_id})
        return pd.read_html(StringIO(html.unescape(res["data"]["table"])))[0]

    def view_dynamictable(self, domain: str, var: str, th: str = "") -> pd.DataFrame:
        res = self._list_pages("data", domain, var=var, th=th)
        datacontent = pd.DataFrame(
            {"key": res["datacontent"].keys(), "value": res["datacontent"].values()}
        ).sort_values("key", ignore_index=True)

        vervar = pd.DataFrame(
            [[x["val"], x["label"]] for x in res["vervar"]],
            columns=["id_var", "variable"],
        ).sort_values("id_var", ignore_index=True)

        turvar = pd.DataFrame(
            [[x["val"], x["label"]] for x in res["turvar"]],
            columns=["id_tur_var", "turunan variable"],
        ).sort_values("id_tur_var", ignore_index=True)

        result = vervar.merge(turvar, how="cross")

        turtahun = None
        if "turtahun" in res:
            turtahun = pd.DataFrame(
                [[x["val"], x["label"]] for x in res["turtahun"]],
                columns=["id_tur_th", "turunan tahun"],
            ).sort_values("id_tur_th", ignore_index=True)
            result = result.merge(turtahun, how="cross")

        tahun = pd.DataFrame(
            [[x["val"], x["label"]] for x in res["tahun"]],
            columns=["val", "label"],
        ).sort_values("val", ignore_index=True)

        for _, year_row in tahun.iterrows():
            result[year_row["label"]] = ""
            for i, row in result.iterrows():
                key_prefix = (
                    str(row["id_var"])
                    + str(var)
                    + str(row["id_tur_var"])
                    + str(year_row["val"])
                    + (str(row["id_tur_th"]) if turtahun is not None else "")
                )
                match = datacontent[datacontent["key"].str.match(f"^{key_prefix}")]["value"]
                if not match.empty:
                    result.at[i, year_row["label"]] = match.iloc[0]

        return result
