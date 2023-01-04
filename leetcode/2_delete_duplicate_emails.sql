# Leetcode (SQL) 196. Delete Duplicate Emails

### 체감 난이도: 2
### DELETE, 같은 테이블 2번 불러와서 활용
### https://leetcode.com/problems/delete-duplicate-emails/description/

DELETE p1 FROM Person p1, Person p2
WHERE p1.email = p2.email
AND p1.id > p2.id