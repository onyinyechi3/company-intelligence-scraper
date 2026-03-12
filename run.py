import pandas as pd
from scrapers.quotes_scraper import scrape_quotes
from validator import validate_dataset


def save_data(data):

    df = pd.DataFrame(data)

    df.to_csv(
        "output/quotes_dataset.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print(f"\nSaved {len(df)} records to dataset.")


def run_pipeline():

    print("Starting scraping pipeline...\n")

    data = scrape_quotes()

    save_data(data)

    print("\nRunning dataset validation...\n")

    validate_dataset()

    print("\nPipeline completed successfully.")


if __name__ == "__main__":

    run_pipeline()