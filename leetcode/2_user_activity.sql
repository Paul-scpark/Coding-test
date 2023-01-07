# Leetcode (SQL) 1141. User Activity for the Past 30 Days I

### 체감 난이도: 2
### COUNT, DISTINCT, BETWEEN, SUBDATE 활용
### https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/

## COUNT, DISTINCT, BETWEEN 활용
# SELECT 
#     activity_date AS day, 
#     COUNT(DISTINCT(user_id)) AS active_users
# FROM Activity
# WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
# GROUP BY activity_date

## COUNT, DISTINCT, BETWEEN, SUBDATE 활용
# SELECT 
#     activity_date AS day, 
#     COUNT(DISTINCT(user_id)) AS active_users
# FROM Activity
# WHERE activity_date BETWEEN SUBDATE('2019-07-27', 29) AND '2019-07-27'
# GROUP BY activity_date

## GROUP BY를 먼저 쓰는 경우
SELECT 
    activity_date AS day, 
    COUNT(DISTINCT(user_id)) AS active_users
FROM Activity
GROUP BY activity_date
HAVING activity_date BETWEEN SUBDATE('2019-07-27', 29) AND '2019-07-27'