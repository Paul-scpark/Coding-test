# Leetcode (SQL) 620. Not Boring Movies

### 체감 난이도: 1
### 나머지 구하기 MOD, != 과 <> 활용
### https://leetcode.com/problems/not-boring-movies/description/

## 나머지를 구하는 MOD가 홀수면, 무조건 1이 나오므로 항상 참이 됨
# SELECT * FROM Cinema
# WHERE description <> 'boring' AND MOD(id, 2)
# ORDER BY rating DESC

## 일치하지 않는 것을 찾는 함수 <>
# SELECT * FROM Cinema
# WHERE description <> 'boring' AND MOD(id, 2) = 1
# ORDER BY rating DESC

SELECT * FROM Cinema
WHERE description != 'boring' AND MOD(id, 2) = 1
ORDER BY rating DESC