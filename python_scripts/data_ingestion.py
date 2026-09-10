import pandas as pd
from pathlib import Path
RAW_DATA_PATH = Path("data/raw")
csv_files = list(RAW_DATA_PATH.glob("*.csv"))
print(f"Found {len(csv_files)} CSV files.")
for file_path in csv_files:
    df = pd.read_csv(file_path)
    print("=" *60)
    print(f"FILE: {file_path.name}")
    print(f"Shape: {df.shape}")
    print("\nData Types:")
    print(df.dtypes)
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())
    if df.isnull().sum().sum() > 0:
        print("\nRows with missing values:")
        print(df[df.isnull().any(axis=1)])
    print("=" *60)