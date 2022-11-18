# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### map, join 함수, 리스트의 인덱스 바꾸기
### https://school.programmers.co.kr/learn/courses/30/lessons/120895?language=python3#

def solution(my_string, num1, num2):
    my_list = list(map(str, my_string))
    my_list[num1], my_list[num2] = my_list[num2], my_list[num1]
    
    return ''.join(my_list)