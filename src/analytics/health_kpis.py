from pathlib import Path

import pandas as pd


SILVER_PATH = Path("data/silver/health_data_clean.csv")
GOLD_PATH = Path("data/gold/kpis.csv")


def load_silver() -> pd.DataFrame:
    """Load the cleaned dataset from the Silver layer."""
    return pd.read_csv(SILVER_PATH)


def build_kpis(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Generate analytical KPIs from the health dataset.

    Current KPI:
    - Total hospitalizations by state.
    """
    return (
        dataframe.groupby("state", as_index=False)
        .agg({"hospitalizations": "sum"})
        .sort_values("hospitalizations", ascending=False)
    )


def save_gold(dataframe: pd.DataFrame) -> None:
    """Persist the KPI dataset into the Gold layer."""
    GOLD_PATH.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(GOLD_PATH, index=False)


def run_analytics() -> None:
    """Execute the Gold analytics pipeline."""
    silver_df = load_silver()
    kpis_df = build_kpis(silver_df)

    save_gold(kpis_df)

    print("✅ Gold layer created")
    print(kpis_df)


if __name__ == "__main__":
    run_analytics()