# 프로그래머스 코딩테스트 연습문제 (힙) - python

### 체감 난이도: 3
### 반복문의 최대 횟수 조정, 시간 복잡도의 중요성, deque
### https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    
    answer = []
    for i in operations:
        target = i.split()[0]
        if target == 'I':
            answer.append(float(i.split()[1]))
        elif target == 'D':
            if i.split()[1] == '1' and len(answer) != 0:
                answer.remove(max(answer))
            if i.split()[1] == '-1' and len(answer) != 0:
                answer.remove(min(answer))
        
    if len(answer) == 0: answer = [0,0]
    else: answer = [max(answer), min(answer)]
    
    return answer