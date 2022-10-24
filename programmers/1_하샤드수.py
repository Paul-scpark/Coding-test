# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list comprehension, is_integer() 함수
### https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    
    if (x / sum([int(i) for i in str(x)])).is_integer():
        return True
    return False