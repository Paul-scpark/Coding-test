# 2019 Kakao Blind Recruitment - python

### 체감 난이도: 2
### list, dict 활용, dict를 key와 value 기준으로 sorting
### https://school.programmers.co.kr/learn/courses/30/lessons/42889#

import numpy as np

def solution(N, stages):
    # stages 리스트를 sorting 후, numpy 객체로 변환
    dic, stages = {}, np.array(sorted(stages))
    
    # 1부터 N까지 for loop을 돌면서 값을 확인
    for i in range(1, N+1):
        # i의 값과 일치하는 것 (현 스테이지 플레이어 수)과 i보다 큰 것 (스테이지에 도달한 플레이어 수) 계산
        # 계산하여 i의 값을 key로 하고, 그 값을 value로 하는 dictionary 객체 생성
        # 스테이지에 도달한 유저가 없는 경우 실패율은 0이므로 try, except 처리
        try: dic[i] = len(stages[stages == i]) / len(stages[stages >= i])
        except: dic[i] = 0
    
    # 최종적으로 생성된 dic에 대하여 value 값을 기준으로 sorting 후, 그 key 값을 리스트로 반환
    return list(dict(sorted(dic.items(), key=lambda item: item[1], reverse=True)).keys())