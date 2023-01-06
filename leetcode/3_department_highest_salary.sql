# Leetcode (SQL) 184. Department Highest Salary

### 체감 난이도: 3
### 서브쿼리, RANK, PARTITION BY, JOIN 활용, 조인 후 컬럼 이름 바꾸기
### https://leetcode.com/problems/department-highest-salary/description/

SELECT T.Department, T.Employee, T.Salary FROM (
    SELECT 
        E.name AS Employee, 
        E.salary AS Salary,
        D.name AS Department, 
        RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee E
    LEFT JOIN Department D
    ON E.departmentId = D.id
) T
WHERE T.salary_rank = 1