# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### 반복문 없이 총합 구하는 방법, range 함수의 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    
    if a > b: a, b = b, a
    
    return sum(range(a, b + 1))