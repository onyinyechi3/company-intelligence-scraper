import pandas as pd
from scrapers.multi_level_scraper import scrape_all_categories
from validator import validate_dataset


def save_data(data):
    df = pd.DataFrame(data)
    df.to_csv(
        "output/company_intelligence_dataset.csv",
        index=False,
        encoding="utf-8-sig"
    )
    print(f"\nSaved {len(df)} records to dataset.")


def run_pipeline():
    print("Starting multi-level scraping pipeline...\n")

    data = scrape_all_categories(limit=5)

    save_data(data)

    print("\nRunning dataset validation...\n")
    validate_dataset("output/company_intelligence_dataset.csv")

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()