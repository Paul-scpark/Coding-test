# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### 수학적 사고
### https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
    
    # k = idx
    # 1 = 0 = 1 - 1
    # 2 = 2 = 2 + 0
    # 3 = 4 = 3 + 1
    # 4 = 6 = 4 + 2
    # 5 = 8 = 5 + 3
    # 6 = 10 = 6 + 4
    
    ## idx = k + k - 2
    
    idx = 2 * (k - 1) % len(numbers)
    return numbers[idx]