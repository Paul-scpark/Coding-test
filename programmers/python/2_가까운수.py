# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### list 활용, 효율적인 코드 짜기
### https://school.programmers.co.kr/learn/courses/30/lessons/120890#

import numpy as np
def solution(array, n):
    array.sort()
    array_diff = np.abs(np.array(array) - n).tolist()
    return array[array_diff.index(min(array_diff))]

#     array.append(n)
#     array.sort()
#     loc = array.index(n)
    
#     if loc == 0:
#         return array[loc + 1]
#     elif loc == len(array) - 1:
#         return array[loc - 1]
#     else:
#         min_value = abs(n - array[loc - 1])
#         max_value = abs(n - array[loc + 1])
#         if max_value < min_value:
#             return array[loc + 1]
#         else: return array[loc - 1]