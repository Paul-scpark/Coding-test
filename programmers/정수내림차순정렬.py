# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### 리스트를 문자열로 만들기 (join 함수)
### https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    
    n_lst = sorted(list(str(n)), reverse = True)
    
    return int(''.join(n_lst))