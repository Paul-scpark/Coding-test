# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### dictionary sorting by key and value
### https://school.programmers.co.kr/learn/courses/30/lessons/120812

from collections import Counter

def solution(array):
    array_dic_sort = dict(sorted(dict(Counter(array)).items(), key=lambda item: item[1]))
    
    last1 = array_dic_sort[list(array_dic_sort.keys())[-1]]
    last2 = 9999
    
    try: last2 = array_dic_sort[list(array_dic_sort.keys())[-2]]
    except: pass

    if last1 == last2:
        return -1
    else:
        return list(array_dic_sort.keys())[-1]