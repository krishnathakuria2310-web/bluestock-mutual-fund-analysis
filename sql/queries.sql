--Top 5 funds by AUM
SELECT
    f.amfi_code,
    f.scheme_name,
    p.aum_crore
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code=f.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;
--Average NAV per month
SELECT
    d.year,
    d.month,
    AVG(n.nav) AS average_nav
FROM fact_nav n
JOIN dim_date d ON n.date_key=d.date_key
GROUP BY d.year,d.month
ORDER BY d.year,d.month;
--SIP YoY growth
SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;
--Transactions by state
SELECT
    state,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_amount_inr
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;
--Funds with expense ratio below 1%
SELECT
    f.scheme_name,
    f.fund_house,
    f.category,
    p.expense_ratio_pct
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code=f.amfi_code
WHERE p.expense_ratio_pct<1
ORDER BY p.expense_ratio_pct;
--Top 5 funds by 3 year return
SELECT
    f.scheme_name,
    f.fund_house,
    p.return_3yr_pct
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code=f.amfi_code
ORDER BY p.return_3yr_pct DESC
LIMIT 5;
--Top 5 funds by Sharpe ratio
SELECT
    f.scheme_name,
    f.fund_house,
    p.sharpe_ratio
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code=f.amfi_code
ORDER BY p.sharpe_ratio DESC
LIMIT 5;
--Top 5 funds by alpha
SELECT
    f.scheme_name,
    f.fund_house,
    p.alpha
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code=f.amfi_code
ORDER BY p.alpha DESC
LIMIT 5;
--AUM by fund house
SELECT
    fund_house,
    SUM(aum_crore) AS total_aum_crore,
    SUM(num_schemes) AS total_schemes
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum_crore DESC;
--Transaction summary by transaction type
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_amount_inr,
    AVG(amount_inr) AS average_amount_inr
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount_inr DESC;