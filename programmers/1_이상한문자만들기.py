# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12930#


def solution(s):

    ### 공백이 여러 개 있는 경우
    answer, idx = '', 0
    for i in s.lower():
        if i != ' ':
            answer += i.upper() if idx % 2 == 0 else i
            idx += 1
        
        elif i == ' ':
            answer += i
            idx = 0
            
    return answer

    # ### 공백이 한 개 있는 경우
    # answer = ''
    # for word in s.lower().split():
    #     for idx, i in enumerate(word):
    #         answer += i.upper() if idx % 2 == 0 else i
    #     answer += ' '

    # return answer[:-1]