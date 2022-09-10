# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### 조건에 맞는 반복문 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12931?language=python3

def solution(n):
    
    answer = 0
    for i in str(n):
        answer += int(i)
        
    return answer