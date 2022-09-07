# 프로그래머스 코딩테스트 연습문제 (스택, 큐) - python

### 체감 난이도: 2
### if ~ else one-line expression
### https://school.programmers.co.kr/learn/courses/30/lessons/12909#

def solution(s):
    
    # '('과 ')'의 개수를 확인해서 0이 되는지 확인
    count = 0
    for i in s:
        if i == '(': count += 1
        elif i == ')': count -= 1
        
        # [예외처리] 만약 count가 0보다 작은 경우에는, ')'가 먼저 나왔으므로 False 리턴
        if count < 0: return False

    return True if count == 0 else False