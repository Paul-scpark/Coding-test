# Leetcode (SQL) 596. Classes More Than 5 Students

### 체감 난이도: 1
### SELECT, FROM, GROUP BY, HAVING, COUNT 활용
### https://leetcode.com/problems/classes-more-than-5-students/?envType=study-plan&id=127644

SELECT class FROM Courses
GROUP BY class HAVING COUNT(class) >= 5