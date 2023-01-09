# Leetcode (SQL) 1965. Employees With Missing Information

### 체감 난이도: 2
### FULL OUTER JOIN (UNION), IS NULL 활용
### https://leetcode.com/problems/employees-with-missing-information/description/

SELECT employee_id
FROM (
    SELECT * FROM Employees left join Salaries USING(employee_id)
    UNION
    SELECT * FROM Employees right join Salaries USING(employee_id)
) T
WHERE T.name IS NULL OR T.salary IS NULL
ORDER BY employee_id