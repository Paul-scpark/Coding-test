# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list, dictionary comprehension
### https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    
    emergency_sort = sorted(emergency, reverse=True)
    dic = {i:idx+1 for idx, i in enumerate(emergency_sort)}
    
    return [dic[i] for i in emergency]