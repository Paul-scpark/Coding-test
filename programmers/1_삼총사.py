# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### 파이썬의 순열 및 조합 (from itertools import combinations)
### https://school.programmers.co.kr/learn/courses/30/lessons/131705

from itertools import combinations
def solution(number):
    answer = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1
            
    return answer