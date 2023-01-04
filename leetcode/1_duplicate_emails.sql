# Leetcode (SQL) 182. Duplicate Emails

### 체감 난이도: 1
### SELECT, FROM, GROUP BY, HAVING 활용
### https://leetcode.com/problems/duplicate-emails/description/

SELECT email AS Email FROM Person
GROUP BY email HAVING COUNT(email) >= 2