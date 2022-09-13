# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list 활용 (sorted, remove 함수)
###https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    
    # [예외 케이스1] arr의 요소가 1개 밖에 없는 경우
    if len(arr) == 1: return [-1]
    
    # 가장 작은 항목을 remove 한 arr를 리턴
    arr.remove(sorted(arr)[0])
    return arr