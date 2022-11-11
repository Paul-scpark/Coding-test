# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### 반복문 활용, 리스트 쪼개기
### https://school.programmers.co.kr/learn/courses/30/lessons/120902#

def solution(my_string):
    my_string = my_string.split()
    
    # 가장 첫 연산자를 통해 계산한 answer 값을 계산해두기
    if my_string[1] == '+':
        answer = int(my_string[0]) + int(my_string[2])
    elif my_string[1] == '-':
        answer = int(my_string[0]) - int(my_string[2])
    
    # 2개의 문자씩 보면서, 첫 문자가 연산자이므로,
    # 해당 연산자에 맞게 answer에 plus or minus를 취해주기
    my_string = my_string[3:]
    for i in range(0, len(my_string) - 1, 2):
        if my_string[i] == '+':
            answer += int(my_string[i + 1])
        elif my_string[i] == '-':
            answer -= int(my_string[i + 1])
    
    return answer