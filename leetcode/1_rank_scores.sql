# Leetcode (SQL) 178. Rank Scores

### 체감 난이도: 1
### RANK, DENSE_RANK 함수 활용
### https://leetcode.com/problems/rank-scores/description/

# RANK          : 공동 순위만큼 건너뜀 (1, 2, 2, 4)
# DENSE_RANK    : 공동 순위를 건너뛰지 않음 (1, 2, 2, 3)
# ROW_NUMBER    : 공동 순위를 무시함 (1, 2, 3, 4)

SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) as 'rank'
FROM Scores