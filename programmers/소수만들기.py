# 프로그래머스 코딩테스트 Summer/Winter Coding (~2018) - python

### 체감 난이도: 2
### itertools 내에 있는 순열 & 조합 함수 활용, 소수 찾기 로직
### https://school.programmers.co.kr/learn/courses/30/lessons/12977#

from itertools import combinations

def solution(nums):
    
    answer = 0
    # 중복을 제거한 상태로 3개씩 조합 생성
    for i in combinations(nums, 3):
        # 생성된 조합들의 합이 소수인지 확인해보기
        value = sum(list(i))
        
        # [소수 찾기 로직] value 값이 1 외에 값과 나눴을 때 0이 나오는게 있다면, 바로 반복문 중지
        idx, flag = 2, True
        while idx != value:
            if value % idx == 0:
                flag = False
                break
            idx += 1
        
        # 반복문을 주어진 모든 조건에 돌았는데, 나눴을 때 0이 되는 값이 없다면 해당 값은 소수
        if flag: answer += 1
        
    return answer