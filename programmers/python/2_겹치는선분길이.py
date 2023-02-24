# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### list comprehension, list intersection
### https://school.programmers.co.kr/learn/courses/30/lessons/120876#

from itertools import combinations

def solution(lines):    
    # 각 선분 별로 range 함수로 길이를 담고 있는 리스트 생성
    lst = [range(i[0], i[1] + 1) for i in lines]

    combination_lst = []
    # 두 개 이상의 선분이 겹쳐야 하므로, combinations 함수 사용
    # range 함수로 되어 있는 두 선분의 교집합을 추출해주기
    # 길이를 담고 있어야 하기 때문에 교집합인 temp의 길이가 1보다 큰 값만 추출
    for i in combinations(lst, 2):
        temp = list(set(i[0]) & set(i[1]))
        if len(temp) > 1:
            combination_lst += temp

    # 최종적으로 추출된 combination_lst에 중복 제거 및 sorting
    # 길이를 계산해야 하므로, 리스트의 길이에 1을 빼서 return
    answer = len(sorted(list(set(combination_lst)))) - 1 
    return answer if answer > 0 else 0