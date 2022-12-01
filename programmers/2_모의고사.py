# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### dict 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    # 주어진 조건대로 학생들의 정답 방식의 기초값을 dict으로 정의
    dic = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    }
    
    dic2 = {}
    # 최대 문제 개수만큼 늘린 후, 주어진 answers의 길이만큼 줄여주기
    for key in dic.keys():
        answer = (dic[key] * 2000)[:len(answers)]
        
        final = 0
        # 학생들의 정답과 주어진 answers가 일치하는 개수 구하기
        for i in range(len(answer)):
            if answer[i] == answers[i]: final += 1
        dic2[key] = final
    
    # 가장 많이 맞춘 학생과 그와 똑같은 점수의 학생들 찾기
    dic2 = dict(sorted(dic2.items(), key=lambda item: item[1], reverse=True))
    top = [list(dic2.items())[0][0]]
    value = list(dic2.items())[0][1]
    
    for i in list(dic2.keys())[1:]:
        if dic2[i] == value: top.append(i)
            
    return top
            