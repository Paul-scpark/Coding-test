# 프로그래머스 코딩테스트 연습문제

### 체감 난이도: 4
### 리스트의 문자열 변환, 문자열의 find & count & replace 함수
### https://school.programmers.co.kr/learn/courses/30/lessons/133502?language=python3#

def solution(ingredient):
    #### [풀이 1] 문자열로 치환하여 find & count & replace 반복하기
    ### 반례: [1, 2, 1, 2, 3, 1, 3, 1, 2, 3, 1, 2, 3, 1]
    ### 이 경우에는 '1231'로 count & replace 해버리기 때문에 정답이 3인데, 2를 출력
#     ## ingredient 값을 문자열로 치환
#     ingredient = str(''.join(str(i) for i in ingredient))
    
#     ## 문자열로 치환한 ingredient 변수에 '1231' 값이 사라질 때까지 반복
#     answer = 0
#     while True:
#         if ingredient.find('1231') != -1:
#             if ingredient.count('1231') != 1:
#                 answer += ingredient.count('1231')
#                 ingredient = ingredient.replace('1231', '')
#             else:
#                 answer += 1
#                 ingredient = ingredient.replace('1231', '', 1)
#         else: break
#     return answer

    #### [풀이 2] 문자열로 치환하여 find & replace 반복하기
    ### 이 경우에는 풀이 1의 반례 사례는 해결했으나, 시간 초과 이슈
#     ## ingredient 값을 문자열로 치환
#     ingredient = str(''.join(str(i) for i in ingredient))
    
#     ## 문자열로 치환한 ingredient 변수에 '1231' 값이 사라질 때까지 반복
#     answer = 0
#     while True:
#         if ingredient.find('1231') != -1:
#             answer += 1
#             ingredient = ingredient.replace('1231', '', 1)
#         else: break
#     return answer

    #### [풀이 3]