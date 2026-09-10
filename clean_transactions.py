import pandas as pd
input_file= "data/raw/1788499980509-304c1255-08_investor_transactions.csv"
df= pd.read_csv(input_file)
df["transaction_date"]= pd.to_datetime(df["transaction_date"])
df["transaction_type"]= df["transaction_type"].str.strip().replace({"sip":"SIP","Sip":"SIP","lumpsum":"Lumpsum","Lumpsum":"Lumpsum","redemption":"Redemption","Redemption":"Redemption"})
valid_types=["SIP","Lumpsum","Redemption"]
invalid_types=df[~df["transaction_type"].isin(valid_types)]
if len(invalid_types)>0:
    print("Invalid transaction types found")
else:
    print("Transaction types are valid")
if (df["amount_inr"]<=0).any():
    print("Invalid transaction amounts found")
else:
    print("All transaction amounts are greater than 0")
valid_kyc=["Verified","Pending"]
invalid_kyc=df[~df["kyc_status"].isin(valid_kyc)]
if len(invalid_kyc)>0:
    print("Invalid KYC status found")
else:
    print("KYC status values are valid")
output_file= "data/processed/investor_transactions.csv"
df.to_csv(output_file,index=False)