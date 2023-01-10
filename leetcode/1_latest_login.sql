# Leetcode (SQL) 1890. The Latest Login in 2020

### 체감 난이도: 1
### YEAR, MAX 활용
### https://leetcode.com/problems/the-latest-login-in-2020/description/

SELECT user_id, MAX(time_stamp) AS last_stamp FROM Logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id