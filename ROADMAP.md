# Roadmap

> The roadmap serves the mission. If an implementation detail conflicts with the compass in README.md, the compass wins. Always.

---

## How to read this

Each phase has a **goal**, a set of **achievables**, and a **gate** — a condition that must be true before moving to the next phase.

Gates are not bureaucratic checkpoints. They are the mission made concrete. If the gate is not passable, the work is not done, regardless of what was built.

There are no deadlines. The instrument becomes true when it is ready, not when a calendar says so.

---

## Phase 0 — Foundation

**Goal:** Lock the compass. Nothing is built until this is solid.

**Achievables:**
- `README.md` — the vision, mission, and sole goals. ✓ Done
- `ROADMAP.md` — this document. ✓ Done
- State variable definition — name and define the 6–8 things the model will track
- CRD schema v0.1 — a YAML specification for variables, plugins, and outputs

**Gate:**
> The schema is reviewable and legible to an economist who has never heard of Kubernetes.

---

## Phase 1 — Proof of Concept

**Goal:** Produce one real number that did not exist before.

**Achievables:**
- Plugin v0.1 — BPS CPI downloader
  - Must reproduce official BPS numbers exactly when fed BPS inputs
  - This is the calibration anchor — if we cannot match BPS, we cannot credibly diverge from it
- Plugin v0.2 — Tokopedia/Shopee sachet scraper
  - Collects sachet vs standard-pack unit prices across core FMCG categories
  - Coverage: 2018 to present
- State estimator v0.1 — simple Kalman filter
  - Two inputs: Plugin v0.1 and Plugin v0.2
  - Produces best estimate of true effective price index for bottom 40%
- Output: sachet premium divergence curve vs official CPI, 2018–2025
  - Confidence intervals shown honestly
  - Data gaps labeled as gaps, not hidden as false certainty
  - Every data point traceable to its source

**Gate:**
> The divergence number and what it means can be explained to a warung owner in Surabaya in under two minutes, without losing accuracy.

---

## Phase 2 — The Instrument

**Goal:** Extend backward in time. More plugins. Honest uncertainty that widens as data thins.

**Achievables:**
- Plugin v0.3 — BPS Susenas household survey implied unit cost
  - Back-infer effective unit costs from household expenditure and quantity data
  - Coverage target: ~2005 onward
- Plugin v0.4 — FMCG public company annual reports pack-size breakdown
  - Unilever Indonesia, Indofood, Wings Group IDX filings
  - Revenue and volume by pack-size tier as proxy for sachet economy scale
  - Coverage target: 2000 onward
- Plugin v0.5 — Kemenkeu cigarette excise data as welfare pressure proxy
  - Brand migration cascade as signal of real disposable income under stress
  - Coverage: wherever excise data is available
- Plugin v0.6 — opportunistic historical sources
  - Wayback Machine retail price recoveries
  - Digitized newspaper market price reports (koran klipping)
  - Each entry: low confidence, explicitly flagged, timestamped
- Ledger layer implementation
  - Every data point carries: source ID, variable, value, timestamp, confidence, known bias flags, ingestion hash
  - Every model update is auditable end-to-end
- Full output: 2000–2025 divergence series
  - Confidence bands widen visibly where data is sparse
  - The uncertainty is part of the result, not a weakness to hide
- Internal peer review
  - Full adversarial review between project and itself
  - Every assumption attacked
  - Every weak data source challenged
  - Document what survives and what was revised

**Gate:**
> The methodology survives an adversarial review. Every number can be challenged specifically — not dismissed generally.

---

## Phase 3 — The Dialogue

**Goal:** Bring the instrument to people who can extend it, and to people who need it.

**Achievables:**
- CELIOS approach
  - Do not pitch an idea — present a result
  - Bring the Phase 1 output: the divergence curve, the methodology, the ledger
  - The ask is not validation — it is collaboration and institutional reach
- Plain language translation layer
  - Every model output expressed in terms people actually live: rupiah amounts, sachets, cigarette brands, warung prices
  - The translation must preserve accuracy — simplification is not permitted to lie
  - If we cannot say it plainly, we do not understand it well enough yet
- Open contribution model
  - Schema is public
  - Anyone can write a plugin that conforms to the spec
  - Contributions add data, narrow uncertainty, extend coverage
  - A researcher in Makassar finding 1998 newspaper price data can submit it
- No fixed timeline for this phase
  - Phase 3 begins when the instrument is ready
  - Readiness is defined by the gate, not by a date

**Gate:**
> This phase has no gate. It is ongoing. The instrument keeps running. The data keeps improving. The explanation keeps getting clearer.

---

## What is not in this roadmap

- Deadlines
- Press releases
- Publication targets
- Grant applications
- A team structure
- A technology stack mandate

These may emerge. They are not the compass.

---

## The one question that governs every decision

> Does this serve the mission of honest measurement explained in plain language?

If yes — proceed.
If no — stop.

---

*This roadmap is a living document. Phases may be revised as the instrument teaches us what it needs. The gates do not move. The mission does not move.*
