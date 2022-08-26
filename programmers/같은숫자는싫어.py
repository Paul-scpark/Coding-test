# 프로그래머스 코딩테스트 연습문제 (스택/큐) - python

### while 무한루프 상에서의 인덱싱, 기본적인 스택/큐 구조
### https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr):
    idx = 0 ; arr_lst = []
    
    # 현재 인덱스와 다음 인덱스가 동일하지 않을 때까지 idx 증가시키고, arr_lst에 값을 append
    while idx != len(arr) - 1:
        if arr[idx] != arr[idx + 1]: 
            arr_lst.append(arr[idx])
        idx += 1
    
    # 가장 마지막 항목은 누락되기 때문에 추가로 붙여주기
    arr_lst.append(arr[-1])
    return arr_lst