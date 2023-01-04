# Leetcode (SQL) 511. Game Play Analysis I

### 체감 난이도: 2
### MIN, GROUP BY, 서브 쿼리, ROW_NUMBER() OVER (PARTITION BY ~ ORDER BY ~) 활용
### https://leetcode.com/problems/game-play-analysis-i/description/

## MIN, GROUP BY 활용
# SELECT player_id, MIN(event_date) AS first_login 
# FROM Activity GROUP BY player_id

## MIN, GROUP BY, DISTINCT 활용
# SELECT DISTINCT player_id, MIN(event_date) AS first_login 
# FROM Activity GROUP BY player_id

## SUB QUERY, ROW_NUMBER() OVER (PARTITION BY ~ ORDER BY ~) 활용
SELECT T.player_id, T.event_date AS first_login
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date asc) AS row_num
    FROM Activity
) AS T WHERE T.row_num = 1