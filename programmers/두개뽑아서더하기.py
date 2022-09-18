# 프로그래머스 월간 코드 챌린지 시즌1 - python

### 체감 난이도: 2
### 순열, 조합 패키지 (from itertools import permutations, combinations)
### https://school.programmers.co.kr/learn/courses/30/lessons/68644

from itertools import permutations

def solution(numbers):
    
    answer_lst = []
    for i in permutations(numbers, 2):
        answer_lst.append(sum(i))
    
    return sorted(list(set(answer_lst)))