# Leetcode (SQL) 1407. Top Travellers

### 체감 난이도: 2
### IFNULL, JOIN, GROUP BY, ORDER BY 활용
### https://leetcode.com/problems/top-travellers/description/

SELECT 
    U.name, 
    IFNULL(SUM(R.distance), 0) AS travelled_distance 
FROM Users U
LEFT JOIN Rides R
ON U.id = R.user_id
GROUP BY U.id
ORDER BY travelled_distance DESC, name