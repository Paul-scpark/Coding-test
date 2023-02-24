# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list에서 원소 찾는 count 함수
### https://school.programmers.co.kr/learn/courses/30/lessons/120912?language=python3

import numpy as np

def solution(array):
    text = ''.join(list(map(str, array)))
    return int((np.array(list(text)) == '7').sum())

    # return ''.join(map(str, array)).count('7')