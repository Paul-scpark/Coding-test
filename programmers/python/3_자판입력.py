# 코딩 테스트 연습문제 - python

### 체감 난이도: 3
### list comprehension, list, set, replace, sum & prod
### list format string to list = ast.literal_eval()
### https://school.programmers.co.kr/learn/courses/30/lessons/160586#

import ast
from math import prod

def solution(keymap, targets):
    ### 전략: targets에 존재하는 unique한 문자들만 찾아, keymap에 존재하는 가장 빠른 index의 값으로 replace 시키고, 그 합을 return
    
    dic, keymap_lst = {}, [list(i) for i in keymap]
    
    # targets에서 unique한 문자들에 대해, keymap에 존재하는 단어 (키)의 index (입력 횟수)를 dict ({키: 입력 횟수}) 형태로 저장
    for i in list(set(list(''.join(targets)))):
        temp = 9999 # 가장 빠른 index를 찾기 위해 갱신시키는 값
        for j in keymap_lst:
            # keymap의 요소들에서 과거에 찾았던 값보다 더 작은 index가 있다면, temp를 갱신
            try:
                if j.index(i) + 1 <= temp:
                    temp = j.index(i) + 1
            except: pass
        
        # 한 번도 나오지 않은 문자가 있는 경우에, (곱으로) 쉽게 처리하도록 temp를 0으로 바꾸기
        if temp == 9999: temp = 0
        dic[i] = temp
    
    # 위에서 만든 dic을 활용하여, targets에 존재하는 문자 (키) 하나씩 입력 횟수로 replace
    targets_str = str([list(i) for i in targets])
    for key in dic.keys():
        targets_str = targets_str.replace(key, str(dic[key]))
    targets_lst = [list(map(int, i)) for i in ast.literal_eval(targets_str)] # 리스트 형태로 변환
    
    # target_lst의 요소들의 곱 (prod)을 했을 때, 0이 나온다는 것은 한 번도 나오지 않은 문자가 있다는 것이므로 -1을 return 
    # 그 외에 경우에는 모두 나왔던 문자이므로, 합 (sum)을 return
    answer = []
    for i in targets_lst:
        answer.append(-1) if prod(i) == 0 else answer.append(sum(i))
            
    return answer