# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list comprehension, permutations
### https://school.programmers.co.kr/learn/courses/30/lessons/120869?language=python3

from itertools import permutations

def solution(spell, dic):
    spell_lst = [''.join(i) for i in permutations(spell, len(spell))]
    
    return 1 if len(set(dic).intersection(set(spell_lst))) >= 1 else 2