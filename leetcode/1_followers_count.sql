# Leetcode (SQL) 1729. Find Followers Count

### 체감 난이도: 1
### SUM과 COUNT, DISTINCT 활용
### https://leetcode.com/problems/find-followers-count/description/

SELECT 
    user_id, 
    COUNT(DISTINCT follower_id) AS followers_count
FROM Followers
GROUP BY user_id