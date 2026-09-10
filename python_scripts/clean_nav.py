import pandas as pd
input_file= "data/raw/1788499983331-4389156d-02_nav_history.csv"
df= pd.read_csv(input_file)
df["date"]= pd.to_datetime(df["date"])
df=df.sort_values(["amfi_code","date"])
df=df.drop_duplicates(subset=["amfi_code","date"])
if (df["nav"]<=0).any():
    print("Invalid NAV values found")
else:
    print("All NAV values are greater than 0")
output_file= "data/processed/nav_history.csv"
df.to_csv(output_file,index=False)