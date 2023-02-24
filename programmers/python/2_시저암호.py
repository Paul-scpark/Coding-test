# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### list의 indexing
### https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    
    answer, alphabet = '', 'abcdefghijklmnopqrstuvwxyz'
    
    for i in s:
        # 공백인 경우
        if i == ' ': 
            answer += ' '

        else:
            # 소문자인 경우
            if i.islower():
                index = (alphabet.index(i) + n) % len(alphabet)
                answer += alphabet[index]
            # 대문자인 경우
            else:
                index = (alphabet.index(i.lower()) + n) % len(alphabet)
                answer += alphabet[index].upper()
    
    return answer