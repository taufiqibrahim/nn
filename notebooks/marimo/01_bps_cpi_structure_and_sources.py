import marimo

__generated_with = "0.23.5"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    # BPS CPI: Structure and Sources

    ## Reasoning

    Opening the BPS CPI table reveals a methodology disclosure before any data:
    at least 7 base year changes since 1966, each with different city coverage,
    different consumption baskets, and different weights.

    This is standard index construction practice. Each rebase reflects an updated
    Survey Biaya Hidup (SBH) — a genuine attempt to keep the basket representative
    of current consumption patterns.

    But the consequence is structural: the series is not continuous. Comparing prices
    across base year boundaries requires explicit splicing methodology. Without it,
    long-run price behavior cannot be read from the published series directly.

    This notebook documents what the measurement instrument actually is before
    attempting to use it.

    ---

    ## Hypotheses

    - [ ] **H1 — Rebase structure:** Document all base years, dates, city counts,
      and basket sources. What does each transition look like at the splice point?

    - [ ] **H2 — Coverage expansion effect:** City coverage expanded from 17 to 90
      over time. How did each expansion change the composition of what gets measured?

    - [ ] **H3 — Basket representation:** Each SBH updates the consumption basket.
      How are small-unit format goods represented relative to their share in
      lower-income household spending?

    - [ ] **H4 — Long-run continuity:** What would a spliced continuous series
      require methodologically? Does BPS or any independent researcher provide one?

    - [ ] **H5 — Recency of standard publications:** What time window do standard
      BPS publications typically cover? What is visible and what requires additional
      work to see?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Primary Source: BPS Methodology Disclosure

    This research started by opening BPS website on https://www.bps.go.id/id.

    ### The Common Steps
    1. Navigate on navbar **Produk** -> **Statistik menurut Subjek**
    2. On the left navigation which is **Subjek** -> Expand **Statistik Ekonomi** -> Click **Harga-Harga**

    Verbatim from BPS IHK table (Keterangan Data):

    > _[PASTE KETERANGAN DATA VERBATIM HERE]_

    Source URL: `[URL]`
    Accessed: `[DATE]`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## H1 — Rebase Structure

    | Base Year | Period Start | Cities | Basket Source | Notes |
    |---|---|---|---|---|
    | 1966=100 | Before Apr 1979 | ? | SBH 1966 | _[FILL]_ |
    | 1977/1978=100 | Apr 1979 | 17 | SBH 1977/1978 | _[FILL]_ |
    | 1988/1989=100 | Apr 1990 | 27 | SBH 1988/1989 | _[FILL]_ |
    | 1996=100 | Dec 1997 | 44 | SBH 1996 | _[FILL]_ |
    | 2002=100 | Jan 2004 | 45 | SBH 2002 | _[FILL]_ |
    | 2007=100 | Jun 2008 | 66 | SBH 2007 | _[FILL]_ |
    | 2012=100 | Jan 2014 | 82 | SBH 2012 | _[FILL]_ |
    | 2018=100 | _[FILL]_ | _[FILL]_ | SBH 2018 | _[FILL]_ |
    | 2022=100 | _[FILL]_ | 90 | SBH 2022 | Current base |

    **Observations:** _[FILL — what patterns do you notice across the transitions?]_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## H2 — Coverage Expansion Effect

    City coverage over time: 17 → 27 → 44 → 45 → 66 → 82 → 90

    **Questions to answer:**
    - Which cities were added at each expansion?
    - What share of informal/peri-urban economy do the added cities represent?
    - Is there documentation of how BPS handled the transition at each expansion?

    **Findings:** _[FILL]_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## H3 — Basket Representation

    Each SBH defines the consumption basket — what goods and services are included
    and with what weights.

    **Questions to answer:**
    - What is the weight of Makanan, Minuman, Tembakau group in each base year?
    - Are small-unit (sachet) format goods listed as separate SKUs or aggregated?
    - What is the methodology for handling product format changes between surveys?

    **Source to check:** SBH methodology documents for each base year.

    **Findings:** _[FILL]_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## H4 — Long-run Continuity

    BPS publishes Table 1 as "2006–2023" — implying some form of chaining
    across the 2012 and 2018 base years.

    **Questions to answer:**
    - What splice methodology does BPS use for this table?
    - Is the splice methodology documented publicly?
    - Does any independent researcher (LPEM, World Bank, IMF) publish a spliced
      series going further back?
    - What does a spliced series from the 1970s to present require?

    **Known sources to check:**
    - BPS: `https://www.bps.go.id/id/statistics-table/2/MiMy/indeks-harga-konsumen--umum-.html`
    - _[ADD others as found]_

    **Findings:** _[FILL]_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## H5 — Recency of Standard Publications

    **Sources inventory:**

    | # | Title | Years Covered | Base | URL | Format | Status |
    |---|---|---|---|---|---|---|
    | 1 | Inflasi 90 kota (umum) | _[FILL]_ | _[FILL]_ | `https://www.bps.go.id/id/statistics-table/2/MTcwOCMy/` | Web table | _[FILL]_ |
    | 2 | Inflasi (umum) | _[FILL]_ | _[FILL]_ | `https://www.bps.go.id/id/statistics-table/2/MSMy/` | Web table | _[FILL]_ |
    | 3 | IHK 90 kota (umum) | _[FILL]_ | _[FILL]_ | `https://www.bps.go.id/id/statistics-table/2/MTcwOSMy/` | Web table | _[FILL]_ |
    | 4 | IHK (umum) | _[FILL]_ | _[FILL]_ | `https://www.bps.go.id/id/statistics-table/2/MiMy/` | Web table | _[FILL]_ |
    | 5 | Tingkat Inflasi Tahunan | _[FILL]_ | 2022=100 | `https://www.bps.go.id/id/statistics-table/1/OTE0IzE=/` | Web table | _[FILL]_ |
    | 6 | Monthly press releases | 2024–present | 2022=100 | `https://www.bps.go.id/en/pressrelease` | PDF + Excel | _[FILL]_ |

    **Gaps identified:** _[FILL — what years or dimensions are not covered by any source?]_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## What This Notebook Established

    _[FILL — summary of what was documented and confirmed]_

    ## What Notebook 02 Needs to Do

    _[FILL — what comes next, based on what was learned here]_

    ## Open Questions

    _[FILL — anything that could not be answered from available sources]_
    """)
    return


if __name__ == "__main__":
    app.run()
