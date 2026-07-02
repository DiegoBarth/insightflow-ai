from src.analytics.health_kpis import run_analytics
from src.ingestion.health_ingestion import run_ingestion
from src.transform.health_transform import run_transformation


def main() -> None:
    """Execute the complete InsightFlow AI pipeline."""

    print("🚀 Starting InsightFlow AI pipeline...\n")

    run_ingestion()
    run_transformation()
    run_analytics()

    print("\n✅ Pipeline finished!")


if __name__ == "__main__":
    main()