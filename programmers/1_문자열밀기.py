# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### 반복문 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120921

def solution(A, B):
    answer = 0
    # A의 길이 만큼만 반복하고, 그 범위 안에서 찾지 못하면 return -1
    for _ in range(len(A)):
        if A == B:
            return answer
        else:
            # 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동
            A = A[-1] + A[:-1]
            answer += 1
    
    return -1