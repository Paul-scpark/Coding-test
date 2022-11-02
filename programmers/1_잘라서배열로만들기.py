# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### for문과 if문 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120913

def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    
    return answer