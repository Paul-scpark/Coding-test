# 프로그래머스 코딩테스트 월간 코드 챌린지 시즌1 - python

### 체감 난이도: 1
### zip 함수의 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    
    answer = 0
    # a와 b를 zip 함수로 불러와서 조건값에 따라 answer 계산
    for i, j in zip(a, b):
        answer += i * j
        
    return answer