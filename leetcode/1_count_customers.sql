# Leetcode (SQL) 1581. Customer Who Visited but Did Not Make Any Transactions

### 체감 난이도: 1
### COUNT, JOIN, USING, GROUP BY 활용
### https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/

SELECT 
    customer_id, 
    COUNT(customer_id) AS count_no_trans
FROM Visits
LEFT JOIN TRANSACTIONS
USING(visit_id)
WHERE transaction_id IS NULL
GROUP BY customer_id