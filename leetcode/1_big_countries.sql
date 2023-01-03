# Leetcode (SQL) 595. Big Countries

### 체감 난이도: 1
### SELECT, FROM, WHERE, OR 활용
### https://leetcode.com/problems/big-countries/?envType=study-plan&id=127644

SELECT name, population, area FROM World
WHERE area >= 3000000 OR population >= 25000000