# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list comprehension
### https://school.programmers.co.kr/learn/courses/30/lessons/120824?language=python3

def solution(num_list):
    a = len([i for i in num_list if i % 2 == 0])
    b = len([i for i in num_list if i % 2 == 1])
    
    return [a, b]