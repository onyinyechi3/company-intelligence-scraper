import pandas as pd

DATA_PATH = "output/quotes_dataset.csv"

def validate_dataset():

    print("Loading dataset...")

    df = pd.read_csv(DATA_PATH)

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
    validate_dataset()