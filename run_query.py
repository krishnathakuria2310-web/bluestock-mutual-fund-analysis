import sqlite3
conn= sqlite3.connect("bluestock_mf.db")
query="""
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_amount_inr,
    AVG(amount_inr) AS average_amount_inr
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount_inr DESC;
"""
result= conn.execute(query).fetchall()
for row in result:
    print(row)
conn.close()