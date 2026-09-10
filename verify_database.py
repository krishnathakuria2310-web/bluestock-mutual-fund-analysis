import pandas as pd
import sqlite3
conn=sqlite3.connect("bluestock_mf.db")
files={
    "dim_fund":"data/processed/fund_master.csv",
    "fact_nav":"data/processed/nav_history.csv",
    "fact_transactions":"data/processed/investor_transactions.csv",
    "fact_performance":"data/processed/scheme_performance.csv",
    "fact_aum":"data/processed/aum_by_fund_house.csv",
    "monthly_sip_inflows":"data/processed/monthly_sip_inflows.csv",
    "category_inflows":"data/processed/category_inflows.csv",
    "industry_folio_count":"data/processed/industry_folio_count.csv",
    "portfolio_holdings":"data/processed/portfolio_holdings.csv",
    "benchmark_indices":"data/processed/benchmark_indices.csv"
}
for table,file in files.items():
    csv_count=len(pd.read_csv(file))
    db_count=conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(table,"CSV:",csv_count,"DB:",db_count,"MATCH:",csv_count==db_count)
conn.close()