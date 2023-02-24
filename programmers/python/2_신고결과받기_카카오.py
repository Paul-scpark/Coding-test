# 2022 KAKAO BLIND RECRUITMENT - python

### 체감 난이도: 2
### 리스트 및 딕셔너리 자료 구조 활용, 리스트 내 중복 제거 (set), numpy 활용 (중복 제거, 인덱싱), 교집합 (intersection), list/dictionary comprehension
### https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=python3

import numpy as np

def solution(id_list, report, k):
    
    # 중복된 항목 제거
    answer, report = [], list(set(report))
    
    # 누구를 신고했는지, 얼마나 신고를 당했는지 확인하는 dic
    attack_dic = {key: [] for key in id_list}
    attacked_dic = {key: 0 for key in id_list}
    
    for user in report:
        attack, attacked = user.split()[0], user.split()[1]
        attack_dic[attack].append(attacked)
        attacked_dic[attacked] += 1
    
    # 신고 당한 횟수가 k보다 큰 항목에 대한 유저만 선택
    mask = np.array(list(attacked_dic.values())) >= k
    target_user = list(np.array(list(attacked_dic.keys()))[mask])
    
    # 신고한 사람들 중, 신고 당한 횟수가 k 보다 큰 유저가 몇 명 있는지 계산
    for user in attack_dic:
        count = len(list(set(target_user).intersection(list(attack_dic[user]))))
        answer.append(count)

    return answer
