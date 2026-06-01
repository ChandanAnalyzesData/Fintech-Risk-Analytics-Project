-- ====================================================================
-- SECTION 1: RELATIONAL DATA ENGINEERING (TABLE JOINS)
-- Purpose: Merge individual transactions with user profile risk scores 
--          to create a unified view for downstream analysis.
-- ====================================================================

SELECT 
    t.transaction_id, 
    t.amount, 
    r.risk_score
FROM Transactions AS t 
INNER JOIN User_Profiles AS r
    ON t.user_id = r.user_id;


-- ====================================================================
-- SECTION 2: HIGH-EXPOSURE RISK AGGREGATION
-- Purpose: Group transactions by status to isolate and surface 
--          operational categories where cumulative loss exceeds 50,000.
-- ====================================================================

SELECT 
    status, 
    SUM(amount) AS total_loss
FROM Transactions
GROUP BY status
HAVING SUM(amount) > 50000;
