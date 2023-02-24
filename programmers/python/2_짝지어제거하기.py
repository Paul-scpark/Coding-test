# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### 수학적 사고, stack & queue 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12973?language=python3#

def solution(s):
    
    # 가장 첫번째 값을 lst에 넣어두고, 그 다음 값부터 for loop으로 확인
    lst = [s[0]]
    for i in s[1:]:
        # lst의 마지막 값이 i의 값과 동일한 경우, 똑같은 문자이므로 lst 마지막 요소 제거
        if len(lst) > 0 and lst[-1] == i:
            lst.pop()
        # lst의 마지막 값과 i가 동일하지 않으면, lst에 i 값을 append
        else:
            lst.append(i)
    
    # 최종적으로 for loop을 모두 돈 후에, lst에 값이 남아있는지 확인
    return 1 if len(lst) == 0 else 0