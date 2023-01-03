# Leetcode (SQL) 181. Employees Earning More Than Their Managers

### 체감 난이도: 2
### 서브 쿼리 활용, 한 테이블 안에서 JOIN 하기
### https://leetcode.com/problems/employees-earning-more-than-their-managers/description/

## 서브 쿼리 활용
# SELECT name as Employee FROM Employee E
# WHERE salary > (
#     SELECT salary FROM Employee
#     WHERE id = E.managerId
# )

## 조인 활용 (조금 더 경제적인 쿼리)
SELECT E1.name as Employee
FROM Employee E1
JOIN Employee E2
ON E1.managerId = E2.id
WHERE E1.salary > E2.salary