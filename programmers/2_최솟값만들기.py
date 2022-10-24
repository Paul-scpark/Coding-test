# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### list의 정렬, reverse, 시간복잡도 고려
### https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    
    # A는 작은 순서대로 정렬, B는 큰 순서대로 정렬
    A_lst = sorted(A)
    B_lst = sorted(B, reverse = True)
    
    # 정렬된 A와 B 리스트를 index 별로 곱해서 최솟값 계산
    answer = 0
    for i in range(len(A)):
        answer += A_lst[i] * B_lst[i]
        
    return answer