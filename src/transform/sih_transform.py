import pandas as pd
from pathlib import Path

BRONZE_PATH = Path("data/bronze/sih_bronze.csv")
SILVER_PATH = Path("data/silver/sih_silver.csv")


def run():
    print("🧹 Transforming SIH data (Silver layer)...")

    df = pd.read_csv(BRONZE_PATH)

    # padronização
    df["state"] = df["state"].str.upper()
    df["city"] = df["city"].str.title()
    df["disease"] = df["disease"].str.lower()
    df["cid_group"] = df["cid_group"].str.upper()
    df["sex"] = df["sex"].str.upper()

    # validações básicas
    df = df.dropna()
    df = df[df["hospitalizations"] > 0]

    SILVER_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(SILVER_PATH, index=False)

    print("✅ Silver layer created")
    print(df.head())


if __name__ == "__main__":
    run()