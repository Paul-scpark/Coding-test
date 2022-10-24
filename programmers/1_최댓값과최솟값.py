# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list comprehension
### https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    
    # 주어진 s가 공백으로 나뉘어져 있으니, split 해서 문자형으로 변환하여 리스트로 저장
    lst = sorted([int(i) for i in s.split()])
    
    return f"{lst[0]} {lst[-1]}"