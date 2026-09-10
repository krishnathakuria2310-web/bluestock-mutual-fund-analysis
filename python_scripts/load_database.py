import pandas as pd
import sqlite3
db_file="bluestock_mf.db"
conn=sqlite3.connect(db_file)
category=pd.read_csv("data/processed/category_inflows.csv")
category["month"]=pd.to_datetime(category["month"]).dt.strftime("%Y-%m-%d")
category.to_sql("category_inflows",conn,if_exists="append",index=False)
industry=pd.read_csv("data/processed/industry_folio_count.csv")
industry["month"]=pd.to_datetime(industry["month"]).dt.strftime("%Y-%m-%d")
industry.to_sql("industry_folio_count",conn,if_exists="append",index=False)
portfolio=pd.read_csv("data/processed/portfolio_holdings.csv")
portfolio["portfolio_date"]=pd.to_datetime(portfolio["portfolio_date"]).dt.strftime("%Y-%m-%d")
portfolio.to_sql("portfolio_holdings",conn,if_exists="append",index=False)
benchmark=pd.read_csv("data/processed/benchmark_indices.csv")
benchmark["date"]=pd.to_datetime(benchmark["date"]).dt.strftime("%Y-%m-%d")
benchmark.to_sql("benchmark_indices",conn,if_exists="append",index=False)
print("All supporting datasets loaded successfully")
conn.close()