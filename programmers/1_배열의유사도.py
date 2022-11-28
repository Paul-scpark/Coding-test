# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### 두 리스트 사이의 교집합 구하기
### https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):
    return len(set(s1).intersection(set(s2)))