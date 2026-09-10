import sqlite3
conn= sqlite3.connect("bluestock_mf.db")
conn.executescript("""
CREATE TABLE category_inflows(
    month DATE,
    category TEXT,
    net_inflow_crore REAL,
    PRIMARY KEY(month,category)
);
CREATE TABLE industry_folio_count(
    month DATE PRIMARY KEY,
    total_folios_crore REAL,
    equity_folios_crore REAL,
    debt_folios_crore REAL,
    hybrid_folios_crore REAL,
    others_folios_crore REAL
);
CREATE TABLE portfolio_holdings(
    amfi_code INTEGER,
    stock_symbol TEXT,
    stock_name TEXT,
    sector TEXT,
    weight_pct REAL,
    market_value_cr REAL,
    current_price_inr REAL,
    portfolio_date DATE,
    PRIMARY KEY(amfi_code,stock_symbol,portfolio_date),
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);
CREATE TABLE benchmark_indices(
    date DATE,
    index_name TEXT,
    close_value REAL,
    PRIMARY KEY(date,index_name)
);
""")
conn.commit()
conn.close()
print("Supporting tables created successfully")