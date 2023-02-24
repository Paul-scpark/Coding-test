# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120904?language=python3

def solution(num, k):
    num_lst = list(map(int, str(num)))
    
    try:
        return num_lst.index(k) + 1
    except:
        return -1