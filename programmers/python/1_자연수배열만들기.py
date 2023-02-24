# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list comprehension, 자연수 뒤집기 (reversed 함수)
### https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    
    n_reversed = str(n)[::-1]
    
    return [int(i) for i in n_reversed]