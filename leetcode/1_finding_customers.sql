# Leetcode (SQL) 586. Customer Placing the Largest Number of Orders

### 체감 난이도: 1
### GROUP BY, ORDER BY, LIMIT 활용
### https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/

SELECT customer_number FROM Orders
GROUP BY customer_number
ORDER BY COUNT(customer_number) DESC
LIMIT 1