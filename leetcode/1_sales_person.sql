# Leetcode (SQL) 607. Sales Person

### 체감 난이도: 1
### 중복 서브 쿼리 활용
### https://leetcode.com/problems/sales-person/description/

SELECT name FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id FROM Orders
    WHERE com_id IN (
        SELECT com_id FROM Company 
        WHERE name = 'RED'
    )
)