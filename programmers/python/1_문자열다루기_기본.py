# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### try & except 활용, isdigit() 함수 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12918?language=python3#

def solution(s):
    # 주어진 s의 길이가 4 또는 6인지 확인
    if (len(s) == 4) or (len(s) == 6):
        # try & except을 통해 숫자 계산이 가능하면 True, 그 외에는 False 리턴
        try: 
            output = int(s) / 2
            return True
        except: return False
    else: return False
    
    ### 다른 사람의 가장 깔끔한 풀이
    ## isdigit() 함수로 숫자인지 확인하고, s의 길이도 함께 확인
    # return s.isdigit() and (len(s) == 4 or len(s) == 6)