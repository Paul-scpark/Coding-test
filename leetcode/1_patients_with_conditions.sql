# Leetcode (SQL) 1527. Patients With a Condition

### 체감 난이도: 1
### LIKE 활용, 문자열의 prefix 값 찾기 
### https://leetcode.com/problems/patients-with-a-condition/description/

SELECT * FROM Patients
WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%'