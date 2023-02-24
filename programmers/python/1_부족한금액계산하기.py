# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### range 함수
### https://school.programmers.co.kr/learn/courses/30/lessons/82612?language=python3

def solution(price, money, count):
    target = price * sum(range(1, count+1))
    return max(target - money, 0)

    # target = price * sum(range(1, count+1))    
    # if target < money: 
    #     return 0
    # return target - money