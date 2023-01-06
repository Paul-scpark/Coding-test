# Leetcode (SQL) 1050. Actors and Directors Who Cooperated At Least Three Times

### 체감 난이도: 1
### 복수의 GROUP BY, HAVING, COUNT 활용
### https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(director_id) >= 3