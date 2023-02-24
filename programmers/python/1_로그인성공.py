# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 1
### for, 조건문 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120883

def solution(id_pw, db):
    
    for i in db:
        if i == id_pw:
            return "login"
        elif i[0] == id_pw[0]:
            return "wrong pw"
    return "fail"