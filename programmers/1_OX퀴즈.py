# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120907?language=python3


def solution(quiz):
    
    answer_lst = []
    for i in quiz:
        lst = i.split()
        answer = int(lst[0]) + int(lst[2]) if lst[1] == '+' else int(lst[0]) - int(lst[2])
            
        if answer == int(lst[-1]): answer_lst.append("O")
        else: answer_lst.append("X")        
        
    return answer_lst