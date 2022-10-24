# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list indexing, 문자열의 곱셈
### https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    
    return '*' * len(phone_number[:-4]) + phone_number[-4:]