# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### Counter 함수 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120896?language=python3

from collections import Counter

def solution(s):
    new_s = ''.join(sorted(s))
    dic = dict(Counter(new_s))
    
    return ''.join([i for i in dic if dic[i] == 1])