# 2022 KAKAO TECH INTERNSHIP - python

### 체감 난이도: 5
### 반복문의 최대 횟수 조정, 시간 복잡도의 중요성, deque
### https://school.programmers.co.kr/learn/courses/30/lessons/118667#

from collections import deque

def solution(queue1, queue2):
    
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    goal = (sum1 + sum2) / 2
    
    # [예외 처리] 각 큐의 원소 합을 같게 만들 수 없는 경우
    if max(queue1 + queue2) > goal: return -1
    
    answer = 0
    while answer <= 600000:
        # 값이 큰 queue의 원소를 작은 queue로 옮기기
        # 매번 sum 함수를 실행하지 않고, plus & minus 수행해주기 (시간 복잡도 고려)
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        # 두 queue의 합이 동일한 경우에 answer를 반환
        else: return answer
        answer += 1

    return -1