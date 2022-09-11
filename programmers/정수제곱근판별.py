# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### math 패키지 활용 (제곱근), is_integer() 함수 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12934

import math

def solution(n):
    
    if math.sqrt(n).is_integer():
        return (math.sqrt(n) + 1) ** 2
    return -1