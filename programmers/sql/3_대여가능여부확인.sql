# 코딩 테스트 연습문제 - sql

### 체감 난이도: 3
### DISTINCT, CASE ~ WHEN ~ THEN, SUB QUERY 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/157340

SELECT DISTINCT(CAR_ID), 
    CASE
        WHEN CAR_ID IN (
            SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
            WHERE DATE('2022-10-16') BETWEEN START_DATE AND END_DATE
        ) THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER BY CAR_ID DESC