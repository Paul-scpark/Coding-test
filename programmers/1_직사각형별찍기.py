# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### map 함수 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12969?language=python3

a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print('*' * a)