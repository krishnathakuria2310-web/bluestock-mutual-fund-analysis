import pandas as pd
input_file= "data/raw/1788499985420-bb134abf-07_scheme_performance.csv"
df= pd.read_csv(input_file)
return_cols=["return_1yr_pct","return_3yr_pct","return_5yr_pct","benchmark_3yr_pct","alpha"]
for col in return_cols:
    df[col]= pd.to_numeric(df[col],errors="coerce")
anomaly_cols=["return_1yr_pct","return_3yr_pct","return_5yr_pct","benchmark_3yr_pct","alpha"]
anomalies=(df[anomaly_cols]<-100)|(df[anomaly_cols]>100)
print("Anomalies found:",anomalies.sum().sum())
if ((df["expense_ratio_pct"]<0.1)|(df["expense_ratio_pct"]>2.5)).any():
    print("Expense ratio outside allowed range")
else:
    print("Expense ratio is within the allowed range")
print("Missing values:",df.isnull().sum().sum())
output_file= "data/processed/scheme_performance.csv"
df.to_csv(output_file,index=False)