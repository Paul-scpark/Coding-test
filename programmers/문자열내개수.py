# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### numpy 패키지 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12916

import numpy as np

def solution(s):
    
    s_array = np.array(list(s.lower()))
    
    p = (s_array == 'p').sum()
    y = (s_array == 'y').sum()
    
    if (p == y) or (p == y == 0):
        return True
    return False