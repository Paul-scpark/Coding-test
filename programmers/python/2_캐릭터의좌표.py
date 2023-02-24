# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### 반례 케이스 추론하기
### https://school.programmers.co.kr/learn/courses/30/lessons/120861?language=python3#

def solution(keyinput, board):
    width, length = board[0] // 2, board[1] // 2
    
    x, y = 0, 0
    for key in keyinput:
        # 위, 아래, 좌, 우 경우에 좌표들 계산해주기
        if key == 'up':
            y += 1
        elif key == 'down':
            y -= 1
        elif key == 'left':
            x -= 1
        elif key == 'right':
            x += 1
        
        # 계산된 좌표가 width, length를 넘는 경우 처리해주기
        if -1 * width > x:
            x = -1 * width
        elif width < x:
            x = width
            
        if -1 * length > y:
            y = -1 * length
        elif length < y:
            y = length
            
    return [x, y]
    

# from collections import Counter
# import numpy as np

#     key_dic = {
#         'up': np.array([0, 1]), 'down': np.array([0, -1]),
#         'left': np.array([-1, 0]), 'right': np.array([1, 0])
#     }
    
#     curr = np.array([0, 0])
#     keyinput_dic = dict(Counter(keyinput))
#     for key in keyinput_dic.keys():        
#         curr += keyinput_dic[key] * key_dic[key]
    
#     print(curr)
    
#     x, y = curr.tolist()[0], curr.tolist()[1]
#     if (-1 * width >= x) and (width <= x):
#         x = x
#     elif -1 * width > x:
#         x = -1 * width
#     elif width < x:
#         x = width
        
#     if (-1 * length >= y) and (length <= y):
#         y = y
#     elif -1 * length > y:
#         y = -1 * length
#     elif length < y:
#         y = length
        
#     return [x, y]