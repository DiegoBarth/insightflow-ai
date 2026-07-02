import pandas as pd
from pathlib import Path

SILVER_PATH = Path("data/silver/sih_silver.csv")
GOLD_PATH = Path("data/gold/sih_kpis.csv")


def run():
    print("📊 Building Health KPIs (Gold layer)...")

    df = pd.read_csv(SILVER_PATH)

    # KPIs principais
    kpis = (
        df.groupby(["state", "disease"], as_index=False)
        .agg(
            total_hospitalizations=("hospitalizations", "sum"),
            avg_cost=("avg_cost", "mean"),
            avg_length_stay=("avg_length_stay", "mean"),
        )
        .sort_values("total_hospitalizations", ascending=False)
    )

    # KPI extra: pressão hospitalar por estado
    state_pressure = (
        df.groupby("state", as_index=False)
        .agg(
            total_hospitalizations=("hospitalizations", "sum"),
            total_cost=("avg_cost", "sum"),
        )
        .sort_values("total_hospitalizations", ascending=False)
    )

    GOLD_PATH.parent.mkdir(parents=True, exist_ok=True)

    kpis.to_csv(GOLD_PATH, index=False)
    state_pressure.to_csv("data/gold/state_pressure.csv", index=False)

    print("✅ Gold layer created")

    print("\n📌 KPIs (top 5):")
    print(kpis.head())


if __name__ == "__main__":
    run()