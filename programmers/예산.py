# 프로그래머스 Summer/Winter Coding (~2018) - python

### 체감 난이도: 1
### list의 sorted 함수, 반복문
### https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    
    d_sum, answer = 0, 0
    # 작은 순서로 정렬한 d에 대해 작은 수부터 한 개씩 더해가기
    for i in sorted(d):
        # 누적해서 더한 d_sum과 다음 인덱스 값을 더한 것이 budget 보다 작을 때까지 반복
        if d_sum + i <= budget:
            d_sum += i
            answer += 1
            
    return answer
            