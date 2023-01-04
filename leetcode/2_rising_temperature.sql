# Leetcode (SQL) 197. Rising Temperature

### 체감 난이도: 2
### DATE 활용 (SUBDATE, DATEDIFF)
### https://leetcode.com/problems/rising-temperature/description/

## JOIN, DATEDIFF 활용
# SELECT w1.id FROM Weather w1
# JOIN Weather w2
# ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
# WHERE w1.temperature > w2.temperature

## JOIN 없이 DATEDIFF만 활용
# SELECT w1.id FROM Weather w1, Weather w2
# WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1
# AND w1.temperature > w2.temperature

## JOIN 없이 SUBDATE만 활용
SELECT w2.id from Weather w1, Weather w2
WHERE SUBDATE(w2.recordDate, 1) = w1.recordDate
AND w2.temperature > w1.temperature