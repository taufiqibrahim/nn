# nn — Roadmap

> The roadmap serves the mission. If an implementation detail conflicts with the compass in README.md, the compass wins. Always.

---

## A note on the name

This project is called `nn` — no name, or close enough to type. `nn` is what you type in the terminal. Neither requires explanation before the work does.

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

**Gate:**
> The variable list is writable on one page and explainable without a diagram.

---

## Phase 1 — Feel the Data

**Goal:** Understand the data before designing anything around it. No schema. No engine. No architecture. Just notebooks, raw sources, and honest exploration.

A schema designed before you have touched the data is fiction. The notebooks will reveal what the data actually is — what is clean, what is missing, what surprises, what the official numbers really mean when you pull them apart. The schema comes after. Not before.

**Achievables:**

*Tier 1 — Directly reproducible (BPS raw → BPS published)*
- Notebook 01 — BPS CPI headline reproduction
  - Pull raw BPS CPI data, reproduce the published monthly headline number exactly
  - This is the calibration anchor: if we cannot match their number with their inputs, we cannot credibly diverge from it
- Notebook 02 — BPS CPI by expenditure group
  - Reproduce Food & Beverages and Processed Food sub-indices specifically
  - This is where the sachet economy lives
- Notebook 03 — BPS CPI by province/city
  - Jakarta vs Surabaya vs Makassar divergence already exists in official data
  - Reproducing it builds the regional pipeline and reveals how much geography matters

*Tier 2 — BPS-adjacent, economists use as standard*
- Notebook 04 — Core vs volatile vs administered price decomposition
  - BPS publishes this breakdown; reproducing it forces understanding of what they classify as "volatile" — mostly food, which is most of what the bottom 40% buys
- Notebook 05 — Susenas implied unit costs
  - Household spending ÷ quantities = implicit unit price per quintile
  - BPS publishes both sides; this is the first direct view into what different income tiers actually pay per gram

*Tier 3 — First divergence: the sachet signal*
- Notebook 06 — Tokopedia/Shopee sachet vs box price scraper
  - Collect sachet vs standard-pack unit prices across core FMCG categories
  - Compute per-gram premium: sachet cost ÷ box cost for equivalent weight
  - Coverage: 2018 to present
- Notebook 07 — First divergence curve
  - Plot Susenas implied unit cost (Notebook 05) vs BPS CPI vs sachet premium (Notebook 06)
  - This is the first number that did not exist before
  - Show confidence intervals honestly. Label gaps as gaps.

*Schema emerges here — not before*
- After notebooks are complete: draft CRD schema v0.1
  - The schema is written from what the data taught, not from what was assumed
  - YAML specification for variables, plugins, and outputs
  - Written to be legible to an economist who has never heard of Kubernetes

**Gate:**
> The divergence number from Notebook 07 can be explained to a warung owner in Surabaya in under two minutes, without losing accuracy. The schema reflects what was learned, not what was planned.

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
- State estimator v0.1 — Kalman filter
  - Fuses all plugin outputs into best estimate of true hidden state
  - Confidence intervals widen where data is sparse — the uncertainty is part of the result, not a weakness to hide
- Full output: 2000–2025 divergence series
- Internal peer review
  - Full adversarial review: every assumption attacked, every weak source challenged
  - Document what survives and what was revised

**Gate:**
> The methodology survives an adversarial review. Every number can be challenged specifically — not dismissed generally.

---

## Phase 2B — The Comparison

**Goal:** Prove the Indonesian signature is structurally abnormal — not just different — by running the same instrument on comparable economies.

A healthy economic loop, when disturbed, oscillates and converges back to equilibrium. Small adjustments. Continuous damping. What the instrument detects in Indonesia is the opposite: long rigidity followed by violent release. Clamped, not stable.

To prove this is a structural failure and not a natural condition, we need a control group. Economies that faced the same disturbances — China import competition, global commodity shocks, post-COVID supply chains — but whose loops show a different signature on the same gauges.

**Why comparison matters:**
- Without it, the findings can be dismissed as a critique of Indonesian policy
- With it, the findings become: *Indonesia is an outlier among comparable economies — and the difference is measurable*
- The comparison is not to rank countries or assign blame. It is to validate the instrument and prove the signal is real

**Comparison economies:**
- **Vietnam** — most critical. Same regional context, same China competition pressure, same padat karya manufacturing base. But wages rose more continuously, prices adjusted more regularly, manufacturing expanded. If Vietnam shows convergent oscillation while Indonesia shows flat-then-snap on the same gauges — that is the proof.
- **Bangladesh** — garment-heavy, similar income tier, similar external pressures. Reveals which specific suppressors matter most by showing a different suppression profile.
- **Thailand 1995–2010** — slightly ahead on the development curve. Shows what a loop looks like as it transitions from suppressed to more freely adjusting.
- **South Korea 1975–1995** — the archetype. A loop that was permitted to oscillate and converge. Wages rose with productivity. Prices adjusted continuously. The result was not magic — it was a loop that was allowed to function.

**Achievables:**
- Plugin v0.7 — comparative economy data ingestion
  - Same variables, same methodology, applied to Vietnam, Bangladesh, Thailand
  - Sources: World Bank microdata, ILO wage surveys, each country's national statistics office
  - Confidence flags applied consistently across all countries
- Oscillation signature analysis
  - For each economy: plot the waveform at each loop node
  - Measure: frequency of adjustment, amplitude of adjustments, convergence behavior after disturbance
- Side-by-side loop health output
  - Same gauge panel, multiple countries, same time period
  - The visual proof: one waveform converges, one does not
  - No statistics degree required to read the difference

**What this proves:**

The loop is not broken by nature. It is broken because specific, identifiable suppressors prevented the continuous small adjustments that allow a loop to self-regulate. Other countries at the same income level, facing the same pressures, show different signatures. The damage was not inevitable. That is what the comparison proves.

**Gate:**
> Side-by-side signatures are legible without explanation. A person who has never studied economics can look at the two waveforms and understand which one is healthy and which one is not.

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
