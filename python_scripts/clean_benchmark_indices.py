import pandas as pd
input_file= "data/raw/1788499982615-f9647ab2-10_benchmark_indices.csv"
df= pd.read_csv(input_file)
df["date"]= pd.to_datetime(df["date"])
df["index_name"]= df["index_name"].str.strip()
df["close_value"]= pd.to_numeric(df["close_value"],errors="coerce")
if df["close_value"].isnull().any():
    print("Invalid close values found")
else:
    print("Close values are valid")
if df.duplicated().any():
    print("Duplicate rows found")
else:
    print("No duplicate rows")
output_file= "data/processed/benchmark_indices.csv"
df.to_csv(output_file,index=False)
print("Benchmark indices cleaned successfully")