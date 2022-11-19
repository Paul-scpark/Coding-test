# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### list comprehension, list intersection
### https://school.programmers.co.kr/learn/courses/30/lessons/120876#

from itertools import combinations

def solution(lines):    
    lst = [range(i[0], i[1] + 1) for i in lines]
    
    combination_lst = []
    for i in combinations(lst, 2):
        temp = list(set(i[0]) & set(i[1]))
        if len(temp) > 1:
            combination_lst += temp
    
    answer = len(sorted(list(set(combination_lst)))) - 1 
    return answer if answer > 0 else 0