# Leetcode (SQL) 1587. Bank Account Summary II

### 체감 난이도: 1
### JOIN, USING, GROUP BY, HAVING 활용
### https://leetcode.com/problems/bank-account-summary-ii/description/

SELECT 
    U.name,
    SUM(T.amount) AS balance
FROM Users U
JOIN TRANSACTIONS T
USING(account)
GROUP BY T.account
HAVING balance > 10000