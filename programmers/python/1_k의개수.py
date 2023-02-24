# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### Counter, map 함수 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120887

from collections import Counter

def solution(i, j, k):
#     answer = 0
#     text = ''.join(map(str, list(range(i, j+1))))
#     for i in text:
#         if i == str(k): answer += 1
#     return answer

    text = ''.join(map(str, list(range(i, j+1))))
    
    try: return dict(Counter(text))[str(k)]
    except: return 0