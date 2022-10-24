# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### numpy 패키지 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12949

import numpy as np

def solution(arr1, arr2):
    
    return (np.dot(np.array(arr1), np.array(arr2))).tolist()