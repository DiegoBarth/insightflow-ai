from src.ingestion.sih_ingestion import run as ingest
from src.transform.sih_transform import run as transform
from src.analytics.sih_kpis import run as analytics


def main():
    print("\n🚀 InsightFlow AI - Health Pipeline\n")

    ingest()
    transform()
    analytics()

    print("\n🏁 Pipeline finished successfully!")


if __name__ == "__main__":
    main()