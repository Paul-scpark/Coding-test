# Leetcode (SQL) 176. Second Highest Salary

### 체감 난이도: 2
### IFNULL, 서브쿼리, RANK, LIMIT, OFFSET 활용
### https://leetcode.com/problems/second-highest-salary/description/

## 실패했던 시도 - IFNULL, 서브쿼리, RANK() 함수 활용해보기
# SELECT IFNULL(
#     (
#         SELECT T1.salary FROM (
#             SELECT *, RANK() OVER (ORDER BY salary DESC) AS row_num
#             FROM Employee
#         ) T1
#         WHERE T1.row_num = 2
#     ), 
#     NULL
# ) AS SecondHighestSalary

## 수정한 쿼리 - IFNULL, 서브쿼리, LIMIT, OFFSET 함수 활용해보기
# 위에서 RANK() OVER (ORDER BY salary DESC)를 LIMIT, OFFSET 함수로 처리 가능
# IFNULL(NAME, "No name"): NAME이 null이라면, "No name" 출력
SELECT IFNULL(
    (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1
    ), NULL
) AS SecondHighestSalary

## MAX 함수, 서브쿼리 활용
# SELECT MAX(salary) AS SecondHighestSalary FROM Employee 
# WHERE salary != (SELECT MAX(salary) FROM Employee)