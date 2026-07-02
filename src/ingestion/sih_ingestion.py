import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/mock/sih_mock.csv")
BRONZE_PATH = Path("data/bronze/sih_bronze.csv")


def run():
    print("📥 Loading SIH mock dataset...")

    df = pd.read_csv(INPUT_PATH)

    BRONZE_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(BRONZE_PATH, index=False)

    print("✅ Bronze layer created")
    print(df.head())


if __name__ == "__main__":
    run()