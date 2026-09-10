import pandas as pd
input_file= "data/raw/1788499984721-4b860901-05_category_inflows.csv"
df= pd.read_csv(input_file)
df["month"]= pd.to_datetime(df["month"])
df["category"]= df["category"].str.strip()
df["net_inflow_crore"]= pd.to_numeric(df["net_inflow_crore"],errors="coerce")
if df["net_inflow_crore"].isnull().any():
    print("Invalid inflow values found")
else:
    print("Inflow values are valid")
if df.duplicated().any():
    print("Duplicate rows found")
else:
    print("No duplicate rows")
output_file= "data/processed/category_inflows.csv"
df.to_csv(output_file,index=False)
print("Category inflows cleaned successfully")