# Leetcode (SQL) 1741. Find Total Time Spent by Each Employee

### 체감 난이도: 1
### SUM 활용
### https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/

SELECT 
    event_day AS day,
    emp_id, 
    SUM(out_time) - SUM(in_time) AS total_time
FROM Employees
GROUP BY emp_id, event_day