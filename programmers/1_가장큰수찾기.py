# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### list 내 가장 큰 수 찾기 Max 함수
### https://school.programmers.co.kr/learn/courses/30/lessons/120899

def solution(array):
    return [max(array), array.index(max(array))]