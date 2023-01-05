# Leetcode (SQL) 627. Swap Salary

### 체감 난이도: 1
### CASE ~ WHEN ~ THEN, IF 함수 활용
### https://leetcode.com/problems/swap-salary/description/

## CASE ~ WHEN ~ THEN 활용
# CASE
# 	WHEN 조건
# 	THEN '반환 값'
# 	WHEN 조건
# 	THEN '반환 값'
# 	ELSE 'WHEN 조건에 해당 안되는 경우 반환 값'
# END

# UPDATE Salary SET sex = 
# CASE
#     WHEN sex = 'm' THEN 'f'
#     WHEN sex = 'f' THEN 'm'
# END

## IF 활용
# IF(조건, '참', '거짓')

UPDATE Salary SET sex = IF(sex = 'f', 'm', 'f')