# 프로그래머스 코딩테스트 월간 코드 챌린지 시즌2 - python

### 체감 난이도: 1
### zip 함수의 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    
    answer = 0
    # absolutes와 signs을 zip 함수로 불러와서 조건값에 따라 answer 계산
    for value, loc in zip(absolutes, signs):
        if not loc: answer += value * -1
        else: answer += value
        
    return answer