# 코딩 테스트 연습문제 - python

### 체감 난이도: 1
### dict 활용 (Counter 함수), dict를 key 또는 value 기준으로 정렬시키기
### https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k, tangerine):
    
    # tangerine에서 반복되었던 숫자만큼 dict를 만들고, value 값을 기준으로 내림차순으로 정렬
    t_dic = dict(Counter(tangerine))
    t_dic_sorted = dict(sorted(t_dic.items(), key=lambda item: item[1], reverse=True))
    
    # 같은 크기의 귤이 많은 것들부터 채워나가면서 box를 한 개씩 증가시키기
    # 단, 귤이 k개 이상 찼다면 반복을 중단해주기
    box, k_sum = 0, 0
    for i in t_dic_sorted.keys():
        k_sum += t_dic_sorted[i]
        box += 1
        
        if k_sum >= k: break
    
    return box