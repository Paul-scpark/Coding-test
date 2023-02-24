# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### if ~ else one-line expression
### https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):

    # [예외 케이스1] num이 1인 경우
    if num == 1: return 0
    
    answer = 0
    while True:
        # 주어진 조건에 따라, 홀수 및 짝수 일때 조건 만들어주기
        num = num / 2 if num % 2 == 0 else (num * 3) + 1    
        answer += 1
        
        # [예외 케이스2] 반복 횟수가 500보다 큰 경우
        if answer >= 500: return -1
    
        # 정답 케이스
        if num == 1: return answer