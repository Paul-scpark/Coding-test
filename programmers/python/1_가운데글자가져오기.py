# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list의 indexing
### https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    
    lens = len(s) // 2
    if len(s) % 2 == 1:
        return s[lens]
    return s[lens - 1 : lens + 1]