# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### for문, if문 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    
    answer = ''
    for _ in range(n // 2):
        answer += '수박'
    
    if n % 2 == 1: answer += '수'
    
    return answer