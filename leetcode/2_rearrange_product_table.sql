# Leetcode (SQL) 1795. Rearrange Products Table

### 체감 난이도: 2
### Tidy 데이터로 변환, IS NOT NULL, UNION 활용
### https://leetcode.com/problems/rearrange-products-table/description/

SELECT product_id, 'store1' AS store, store1 AS price 
FROM Products 
WHERE store1 IS NOT NULL
UNION 
SELECT product_id, 'store2' AS store, store2 AS price 
FROM Products 
WHERE store2 IS NOT NULL
UNION 
SELECT product_id, 'store3' AS store, store3 AS price 
FROM Products 
WHERE store3 IS NOT NULL