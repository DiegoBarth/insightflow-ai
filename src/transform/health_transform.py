from pathlib import Path

import pandas as pd


BRONZE_PATH = Path("data/bronze/health_data.csv")
SILVER_PATH = Path("data/silver/health_data_clean.csv")


def load_bronze() -> pd.DataFrame:
    """Load the dataset from the Bronze layer."""
    return pd.read_csv(BRONZE_PATH)


def clean_health_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and normalize health data.

    Current transformations:
    - Normalize state names
    - Remove rows with missing values
    """
    clean_df = dataframe.copy()

    clean_df["state"] = clean_df["state"].str.upper()
    clean_df = clean_df.dropna()

    return clean_df


def save_silver(dataframe: pd.DataFrame) -> None:
    """Persist the cleaned dataset into the Silver layer."""
    SILVER_PATH.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(SILVER_PATH, index=False)


def run_transformation() -> None:
    """Execute the Silver transformation pipeline."""
    bronze_df = load_bronze()
    silver_df = clean_health_data(bronze_df)

    save_silver(silver_df)

    print("✅ Silver layer created")


if __name__ == "__main__":
    run_transformation()