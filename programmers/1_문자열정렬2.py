# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### lower, sorted, join 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120911

def solution(my_string):
    return ''.join(sorted(my_string.lower()))