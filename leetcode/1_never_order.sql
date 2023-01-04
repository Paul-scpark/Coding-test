# Leetcode (SQL) 183. Customers Who Never Order

### 체감 난이도: 1
### LEFT JOIN, IS NULL 활용
### https://leetcode.com/problems/customers-who-never-order/description/

SELECT name AS Customers FROM Customers C
LEFT JOIN Orders O
ON C.id = O.customerId
WHERE O.customerId IS NULL