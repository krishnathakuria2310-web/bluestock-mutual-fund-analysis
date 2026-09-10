import pandas as pd
input_file= "data/raw/1788499984405-d702a6c6-04_monthly_sip_inflows.csv"
df= pd.read_csv(input_file)
df["month"]= pd.to_datetime(df["month"])
numeric_cols=["sip_inflow_crore","active_sip_accounts_crore","new_sip_accounts_lakh","sip_aum_lakh_crore","yoy_growth_pct"]
for col in numeric_cols:
    df[col]= pd.to_numeric(df[col],errors="coerce")
if (df["sip_inflow_crore"]<0).any():
    print("Invalid SIP inflow values found")
else:
    print("SIP inflow values are valid")
if df["yoy_growth_pct"].isnull().sum()>0:
    print("Missing YoY values:",df["yoy_growth_pct"].isnull().sum())
else:
    print("No missing YoY values")
output_file= "data/processed/monthly_sip_inflows.csv"
df.to_csv(output_file,index=False)
print("SIP inflow data cleaned successfully")