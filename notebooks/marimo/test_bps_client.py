import marimo

__generated_with = "0.23.5"
app = marimo.App()


@app.cell
def _():
    import os
    from pathlib import Path
    from dotenv import load_dotenv
    from nn.signals.bps.client import BPSWebApiClient, to_df, normalize_date

    load_dotenv(Path(__file__).parent / "../../.env")

    client = BPSWebApiClient(os.environ["BPS_WEB_API_TOKEN"])
    return client, normalize_date, to_df


@app.cell
def _(client, to_df):
    domains = client.list_domain()
    domains = to_df(domains)
    domains
    return


@app.cell
def _(client, to_df):
    subjects = client.list_subject()
    subjects = to_df(subjects)
    subjects
    return


@app.cell
def _(client, to_df):
    subject_categories = client.list_subject_categories()
    subject_categories = to_df(subject_categories)
    subject_categories
    return


@app.cell
def _(client, to_df):
    variables = client.list_variable(domain="0000", subject="3")
    variables = to_df(variables)
    variables
    return


@app.cell
def _(client, to_df):
    periods = client.list_period(domain="0000", var="1890")
    periods = to_df(periods)
    periods
    return


@app.cell
def _(client, normalize_date):
    data = client.get_data(domain="0000", var="1890", th="121")
    data = normalize_date(data)
    return (data,)


@app.cell
def _(data):
    data.sort_values(["variable", "turvar", "ds"])
    return


if __name__ == "__main__":
    app.run()
