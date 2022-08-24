# 프로그래머스 코딩테스트 연습문제 - python

### numpy를 list로 변환 (tolist)
### https://school.programmers.co.kr/learn/courses/30/lessons/12950?language=python3

import numpy as np

def solution(arr1, arr2):
    
    answer = []
    
    # numpy 패키지를 통해 행렬의 덧셈 연산 수행 후, list로 변환
    for i in list(np.array(arr1) + np.array(arr2)):
        answer.append(i.tolist())
        
    return answer