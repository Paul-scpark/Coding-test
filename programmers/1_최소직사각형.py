# 프로그래머스 코딩테스트 연습문제 (완전탐색) - python

### 체감 난이도: 1
### 리스트 내에 최대, 최솟값 찾기 (max, min)
### https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3

def solution(sizes):
    
    # 배열 내에서 가장 큰 값이 있는 리스트 추출    
    max_idx, max_value = 0, 0
    for idx in range(len(sizes)):
        if max_value < max(sizes[idx]):
            max_value = max(sizes[idx])
            max_idx = idx
    
    # 추출한 리스트에서 더 작은 값을 선택하고, 각 리스트들의 더 작은 값과 비교하여 가장 큰 값으로 대체
    min_value = min(sizes[max_idx])
    for i in sizes:
        if min_value < min(i):
            min_value = min(i)
            
    return max_value * min_value