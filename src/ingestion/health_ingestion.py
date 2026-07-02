from pathlib import Path

import pandas as pd

BRONZE_PATH = Path("data/bronze/health_data.csv")


def fetch_health_data() -> pd.DataFrame:
    """
    Simulate the ingestion of public health data.

    This function will later be replaced by a real data source
    such as DATASUS or another public API.
    """
    return pd.DataFrame(
        {
            "state": ["PR", "SP", "RJ", "MG", "RS"],
            "year": [2023, 2023, 2023, 2023, 2023],
            "hospitalizations": [1200, 5400, 3200, 2100, 1800],
        }
    )


def save_bronze(dataframe: pd.DataFrame) -> None:
    """Persist the raw dataset into the Bronze layer."""
    BRONZE_PATH.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(BRONZE_PATH, index=False)


def run_ingestion() -> None:
    """Execute the Bronze ingestion pipeline."""
    health_df = fetch_health_data()
    save_bronze(health_df)

    print("✅ Bronze layer created")


if __name__ == "__main__":
    run_ingestion()