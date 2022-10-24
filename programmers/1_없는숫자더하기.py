# 프로그래머스 코딩테스트 월간 코드 챌린지 시즌3 - python

### 체감 난이도: 1
### numpy를 이용한 array의 합
### https://school.programmers.co.kr/learn/courses/30/lessons/86051?language=python3

import numpy as np

def solution(numbers):
    
    # 0부터 9까지의 모든 숫자의 합은 45
    # 현재 주어진 리스트의 합에서 45를 뺴면, 비어있는 원소들의 합 도출 가능
    return 45 - int(np.array(numbers).sum())