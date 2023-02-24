# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### list comprehension, convert string to list and vice versa
### https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    return ''.join([i * n for i in list(my_string)])