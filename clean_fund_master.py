import pandas as pd
input_file= "data/raw/1788499983024-b042c300-01_fund_master.csv"
df= pd.read_csv(input_file)
df["launch_date"]= pd.to_datetime(df["launch_date"])
text_cols=["fund_house","scheme_name","category","sub_category","plan","benchmark","fund_manager","risk_category","sebi_category_code"]
for col in text_cols:
    df[col]= df[col].str.strip()
if df["amfi_code"].duplicated().any():
    print("Duplicate AMFI codes found")
else:
    print("AMFI codes are unique")
if df.isnull().sum().sum()>0:
    print("Missing values found")
else:
    print("No missing values")
output_file= "data/processed/fund_master.csv"
df.to_csv(output_file,index=False)
print("Fund master cleaned successfully")