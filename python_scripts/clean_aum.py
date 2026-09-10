import pandas as pd
input_file= "data/raw/1788499984134-b0cbf625-03_aum_by_fund_house.csv"
df= pd.read_csv(input_file)
df["date"]= pd.to_datetime(df["date"])
df["fund_house"]= df["fund_house"].str.strip()
df["aum_crore"]= pd.to_numeric(df["aum_crore"],errors="coerce")
df["aum_lakh_crore"]= pd.to_numeric(df["aum_lakh_crore"],errors="coerce")
df["num_schemes"]= pd.to_numeric(df["num_schemes"],errors="coerce")
if df.isnull().sum().sum()>0:
    print("Invalid or missing values found")
else:
    print("AUM values are valid")
output_file= "data/processed/aum_by_fund_house.csv"
df.to_csv(output_file,index=False)
print("AUM data cleaned successfully")