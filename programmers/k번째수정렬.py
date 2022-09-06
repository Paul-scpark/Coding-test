# 프로그래머스 코딩테스트 연습문제 (정렬) - python

### 체감 난이도: 1
### list 인덱싱, sorted 함수
### https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    
    answer_lst = []
    for i, j, k in commands:
        # 주어진 command 조건에 따라 인덱싱 및 k번째 값 추출
        sort_lst = sorted(array[i-1:j])
        answer_lst.append(sort_lst[k-1])
        
    return answer_lst