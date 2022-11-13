# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### 문제의 정확한 이해, 스택 & 큐
### https://school.programmers.co.kr/learn/courses/30/lessons/120853#

def solution(s):
    
    answer_lst = []
    for i in s.split():
        if (i == 'Z') and (len(answer_lst) != 0):
            answer_lst.pop()
        elif i != 'Z':
            answer_lst.append(int(i))
    
    return sum(answer_lst)