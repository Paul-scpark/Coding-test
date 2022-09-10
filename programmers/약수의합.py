# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### 조건에 맞는 반복문 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    
    i, answer_lst = 1, []
    
    # 약수의 최댓값은 n 자체까지 도달할 수 있음
    while i != n + 1:
        # n이 i로 나눠서 0이 되면, 약수이므로 answer_lst에 추가
        if n % i == 0:
            answer_lst.append(i)
        i += 1
        
    return sum(answer_lst)