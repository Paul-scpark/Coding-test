# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### sorted 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120886

def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0