# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### join 함수, list의 정렬
### https://school.programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    
    return ''.join(sorted(list(s), reverse = True))