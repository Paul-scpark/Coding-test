# Leetcode (SQL) 584. Find Customer Referee

### 체감 난이도: 1
### IS NULL, IS NOT NULL
### https://leetcode.com/problems/find-customer-referee/

SELECT name FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL