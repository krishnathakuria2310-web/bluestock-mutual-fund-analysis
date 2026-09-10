import pandas as pd
input_file= "data/raw/1788499982117-e3d6ab98-09_portfolio_holdings.csv"
df= pd.read_csv(input_file)
df["portfolio_date"]= pd.to_datetime(df["portfolio_date"])
text_cols=["stock_symbol","stock_name","sector"]
for col in text_cols:
    df[col]= df[col].str.strip()
if ((df["weight_pct"]<0)|(df["weight_pct"]>100)).any():
    print("Invalid weight values found")
else:
    print("Weight values are valid")
if (df["market_value_cr"]<0).any():
    print("Invalid market values found")
else:
    print("Market values are valid")
if (df["current_price_inr"]<=0).any():
    print("Invalid price values found")
else:
    print("Price values are valid")
output_file= "data/processed/portfolio_holdings.csv"
df.to_csv(output_file,index=False)
print("Portfolio holdings cleaned successfully")