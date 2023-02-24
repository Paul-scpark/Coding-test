# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    lst = []
    for i in my_string:
        if i not in lst: lst.append(i)
    
    return ''.join(lst)