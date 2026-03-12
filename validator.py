import pandas as pd


def validate_dataset(file_path):
    print("Loading dataset...")

    df = pd.read_csv(file_path)

    print("\nDataset Overview")
    print("----------------")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nSample Data:")
    print(df.head())

    print("\nValidation Complete.")


if __name__ == "__main__":
    validate_dataset("output/company_intelligence_dataset.csv")