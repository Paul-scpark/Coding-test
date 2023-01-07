# Leetcode (SQL) 1084. Sales Analysis III

### 체감 난이도: 2
### JOIN 시에 ON 대신 USING 사용 가능, GROUP BY ~ HAVING, BETWEEN 함수 활용
### https://leetcode.com/problems/sales-analysis-iii/description/

## BETWEEN 활용 (value1과 value2 사이의 범위 추리기 - 이상, 이하)
## 앞에 오는 값 (value1)이 뒤에 오는 값 (value2) 보다 작아야 함
# WHERE col_name BETWEEN value1 AND value2

SELECT product_id, product_name
FROM Product
LEFT JOIN Sales
USING(product_id)  # ON P.product_id = S.product_id
GROUP BY product_id
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'