# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### 조건에 맞는 반복문 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    
    i = 2
    while (n - 1) % i != 0:
        i += 1
    
    return i