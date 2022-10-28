# 프로그래머스 코딩테스트 연습문제

### 체감 난이도: 4
### 리스트의 문자열 변환, 문자열의 find & count & replace 함수
### https://school.programmers.co.kr/learn/courses/30/lessons/133502?language=python3#

def solution(ingredient):
    ### 문자열로 치환하여 replace & find 반복하기
    ## ingredient 값을 문자열로 치환
    ingredient = str(''.join(str(i) for i in ingredient))
    
    ## 문자열로 치환한 ingredient 변수에 '1231' 값이 사라질 때까지 반복
    answer = 0
    while True:
        if ingredient.find('1231') != -1:
            if ingredient.count('1231') != 1:
                answer += ingredient.count('1231')
                ingredient = ingredient.replace('1231', '')
            else:
                answer += 1
                ingredient = ingredient.replace('1231', '', 1)
        else: break
    return answer