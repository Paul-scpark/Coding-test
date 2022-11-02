# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### for문과 if문 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120842?language=python3

def solution(num_list, n):
    temp, answer = [], []
    for i in num_list:
        temp.append(i)
        
        if len(temp) == n:
            answer.append(temp)
            temp = []
            
    return answer