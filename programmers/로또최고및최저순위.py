# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### list 내에서의 count 함수, numpy 패키지 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/77484#fnref1

import numpy as np

def solve(score):
    if score < 2:
        return 6
    return 7 - score

def solution(lottos, win_nums):
    
    # 구매한 로또 번호 중에 0의 개수 확인
    count_0 = (np.array(lottos) == 0).sum()
    
    # 구매한 로또 번호 중에 일치하는 번호 개수 확인
    answer = 0
    for i in lottos:
        if i in win_nums:
            answer += 1
    
    # 0의 개수를 통해서 최대 점수와 최대 점수 계산
    max_score = answer + count_0
    min_score = answer
    
    return [int(solve(max_score)), int(solve(min_score))]
