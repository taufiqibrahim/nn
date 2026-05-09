# You’re Building a Signal Intelligence System

Not a CRUD app.
Not just data pipelines.
Not merely API clients.

You are building a system that converts observations from the world into actionable intelligence.

# Real Conceptual Architecture

```text id="8ry8s5"
Sources emit signals
        ↓
Signals are normalized
        ↓
Hidden ledger stores truth/history/confidence
        ↓
Intelligence layer interprets patterns
        ↓
Services expose useful products
```

# Canonical Flow

```text id="6i8db4"
BPS releases CPI
JISDOR updates FX
Retail observer says kopi sachet naik
Rainfall anomaly reported
Commodity feed moves higher

All become SIGNALS
        ↓
Ledger
        ↓
Signals Intelligence
        ↓
API / Alerts / Reports / Dashboards
```

# Core Ontology (Final Language)

Use these terms consistently.

## External World

```text id="7o2d55"
Source
```

Examples:

* BPS
* Bank Indonesia
* TradingEconomics
* field enumerator
* retail monitor
* manual analyst note

## Incoming Unit of Information

```text id="t8jowr"
Signal
```

Examples:

* CPI rose 0.8%
* Harga kopi sachet naik Rp500
* Rice stock thinning
* Rupiah weakens 1.2%

## Internal Truth Engine (Hidden)

```text id="1iv16y"
Ledger
```

Stores:

* normalized records
* history
* revisions
* confidence
* provenance
* deduplication
* reconciliation

Users should not interact with ledger directly.

## Derived Value Layer

```text id="7f9up2"
Intelligence
```

Examples:

* inflation pressure increasing
* supply stress emerging
* FX pass-through risk elevated
* likely CPI acceleration next month

## User-Facing Layer

```text id="wq4v0k"
Services
```

Examples:

* API
* alerts
* reports
* dashboards
* notebooks

# Final Repository Structure

```text id="pjmdpw"
nn/
├── signals/
│   ├── official/
│   │   ├── bps/
│   │   ├── jisdor/
│   │   └── worldbank/
│   │
│   ├── market/
│   │   ├── retail_prices/
│   │   └── commodities/
│   │
│   ├── observed/
│   │   ├── field_reports/
│   │   └── manual_notes/
│   │
│   └── shared/
│
├── ledger/
│   ├── models.py
│   ├── writer.py
│   ├── reader.py
│   └── reconcile.py
│
├── intelligence/
│   ├── inflation.py
│   ├── shortages.py
│   ├── fx_pressure.py
│   └── anomaly.py
│
├── services/
│   ├── api/
│   ├── alerts/
│   ├── reports/
│   └── dashboards/
│
└── core/
    ├── config.py
    ├── db.py
    └── logging.py
```

# Final BPS Module Shape

```text id="cwn2zr"
nn/signals/official/bps/
├── client.py
├── signals.py
└── schemas.py
```

# Naming Rules (Final)

## Good

```text id="73o7iz"
signals.py
client.py
adapter.py
ledger.py
reconcile.py
inflation.py
alerts.py
```

## Avoid

```text id="vllc2g"
utils.py
helpers.py
misc.py
source.py   # misleading if file is code not actual source
provider_data.py
```

# Why `source.py` Was Rejected

Because BPS is the source.
A Python file is not the source.

Use:

```text id="ev7ey2"
client.py   # talks to source
signals.py  # emits signals
```

# Example Mental Model

```python id="xxxtv2"
client = BPSClient()
signals = BPSSignals(client).cpi()
ledger.write(signals)
insight = InflationIntel().evaluate()
```

# Product Language (Very Important)

Never expose internals like:

```text id="0hqdx4"
table_rows
records
provider_payload
```

Expose:

```text id="h9fsgf"
Signals
Confidence
Trend
Risk
Pressure
Outlook
Alert
```

# Strategic Moat

Your moat is **not** fetching BPS data.

Your moat is:

```text id="uhbkwf"
Combining many weak signals into trusted intelligence.
```

# If This Grows Large Later

Split by bounded contexts:

```text id="j5i5hx"
nn-signals
nn-ledger
nn-intelligence
nn-services
```

But stay monolith now.

# Final One-Line Identity

```text id="6n8xb5"
NN is a signal intelligence platform powered by a hidden truth ledger.
```

# Final Advice

Design every new feature by asking:

```text id="n7rmbr"
Is this a source?
Is this a signal?
Does it belong in ledger?
Is it intelligence?
Or is it a service?
```

That question alone will keep architecture clean for years.
