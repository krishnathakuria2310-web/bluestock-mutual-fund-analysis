import pandas as pd
input_file= "data/raw/1788499985036-da4a0c4a-06_industry_folio_count.csv"
df= pd.read_csv(input_file)
df["month"]= pd.to_datetime(df["month"])
numeric_cols=["total_folios_crore","equity_folios_crore","debt_folios_crore","hybrid_folios_crore","others_folios_crore"]
for col in numeric_cols:
    df[col]= pd.to_numeric(df[col],errors="coerce")
if df.isnull().sum().sum()>0:
    print("Missing or invalid values found")
else:
    print("Folio values are valid")
if df.duplicated().any():
    print("Duplicate rows found")
else:
    print("No duplicate rows")
output_file= "data/processed/industry_folio_count.csv"
df.to_csv(output_file,index=False)
print("Industry folio data cleaned successfully")