# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### enumerate, indexing 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    for idx, i in enumerate(food[1:]):
        answer += str(idx+1) * (i//2)
        
    return answer + '0' + ''.join(list(reversed(answer)))