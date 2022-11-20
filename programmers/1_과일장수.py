# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list comprehension, list indexing
### https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    score = sorted([i for i in score if i <= k], reverse=True)
    
    answer, start = 0, 0
    while start <= len(score) - 1:
        lst = score[start:start+m]
        if len(lst) == m: answer += min(lst) * len(lst)
        start += m
    
    return answer