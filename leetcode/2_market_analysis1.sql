# Leetcode (SQL) 1158. Market Analysis I

### 체감 난이도: 2
### JOIN 할 때 서브쿼리 사용하기, COUNT, GROUP BY 등 활용
### https://leetcode.com/problems/market-analysis-i/description/

SELECT 
    user_id AS buyer_id, 
    join_date, 
    COUNT(order_id) AS orders_in_2019 
FROM Users U
LEFT JOIN (
    SELECT * FROM Orders
    WHERE YEAR(order_date) = '2019'
) O
ON U.user_id = O.buyer_id
GROUP BY user_id