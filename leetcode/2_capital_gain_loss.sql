# Leetcode (SQL) 1393. Capital Gain/Loss

### 체감 난이도: 2
### CASE ~ THEN, SUM & IF 함수 활용
### https://leetcode.com/problems/capital-gainloss/description/

## CASE ~ THEN 활용
# SELECT stock_name, SUM(
#     CASE
#         WHEN operation = 'Buy' THEN -price
#         ELSE price
#     END
# ) AS capital_gain_loss
# FROM Stocks
# GROUP BY stock_name

## SUM, IF 활용
SELECT stock_name, SUM(IF(operation='Buy', -price, price)) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name