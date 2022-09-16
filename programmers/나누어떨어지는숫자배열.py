# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### numpy 패키지 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12910

import numpy as np

def solution(arr, divisor):
    
    answer_lst = []
    # numpy 배열로 변환하여 각 element를 divisor로 나눠주기
    for i in (np.array(sorted(arr)) / divisor).tolist():
        # 나눈 결과가 integer인 경우에 answer_lst에 추가
        if i.is_integer():
            answer_lst.append(i * divisor)
            
    if len(answer_lst) == 0:
        return [-1]
    return answer_lst