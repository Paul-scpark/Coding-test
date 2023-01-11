# Leetcode (SQL) 1667. Fix Names in a Table

### 체감 난이도: 2
### SUBSTR, UPPER, LOWER, CONCAT 활용
### https://leetcode.com/problems/fix-names-in-a-table/description/

## SUBSTR: 문자열 일부 자르기
# SUBSTR(대상 문자열, 시작 위치, 길이)
# 위치 파라미터를 생략하는 경우에는 가장 마지막까지가 Default 값

## CONCAT: 문자열 합치기 (붙이기)
# CONCAT(합치고자 하는 문자열1, 합치고자 하는 문자열2, ...)

SELECT 
    user_id,
    CONCAT(UPPER(SUBSTR(name, 1, 1)), LOWER(SUBSTR(name, 2))) AS name
FROM Users
ORDER BY user_id