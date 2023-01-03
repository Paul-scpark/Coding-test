# Leetcode (SQL) 175. Combine Two Tables

### 체감 난이도: 1
### 두 개 테이블 JOIN (LEFT, RIGHT)
### https://leetcode.com/problems/combine-two-tables/description/

SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P LEFT JOIN Address A
on P.personId = A.personId