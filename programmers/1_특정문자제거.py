# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### array filtering, replace
### https://school.programmers.co.kr/learn/courses/30/lessons/120826

import numpy as np

def solution(my_string, letter):
    arr = np.array(list(my_string))
    return ''.join(arr[arr != letter])

    # return my_string.replace(letter, '')