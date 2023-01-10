# Leetcode (SQL) 1873. Calculate Special Bonus

### 체감 난이도: 2
### SUBSTR, MOD, UNION, IF, CASE ~ THEN 활용
### https://leetcode.com/problems/calculate-special-bonus/description/

## UNION을 통해 두 가지 경우의 수를 합해서 결과 도출하기
-- SELECT employee_id, salary * 0 AS bonus FROM Employees
-- WHERE employee_id IN (
--     SELECT employee_id FROM Employees
--     WHERE 
--         SUBSTR(name, 1, 1) = 'M' OR 
--         MOD(employee_id, 2) = 0
-- )
-- UNION
-- SELECT employee_id, salary AS bonus FROM Employees
-- WHERE employee_id NOT IN (
--     SELECT employee_id FROM Employees
--     WHERE 
--         SUBSTR(name, 1, 1) = 'M' OR 
--         MOD(employee_id, 2) = 0
-- )
-- ORDER BY employee_id

## IF 함수를 통해 조건을 하나로 묶어주기
-- SELECT 
--     employee_id, 
--     if(employee_id % 2 != 0 AND name NOT LIKE 'M%', salary, 0) AS bonus
-- FROM Employees
-- ORDER BY employee_id

## 위의 IF 함수를 CASE ~ THEN으로 표현 가능
SELECT employee_id,
CASE 
    when employee_id % 2 != 0 AND name NOT LIKE 'M%' then salary
    else 0
END AS bonus
FROM Employees
ORDER BY employee_id