# 코딩 테스트 연습문제 - python

### 체감 난이도: 2
### indexing, 조건에 따른 반복문 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/155652?language=python3#

def solution(s, skip, index):
    
    answer, alphabet = '', list('abcdefghijklmnopqrstuvwxyz')
    
    # s의 문자열을 하나씩 읽으며, index 만큼 떨어져 있으면서 skip에 겹치지 않는 answer 값을 return
    for i in s:
        idx = alphabet.index(i)
        
        # index 만큼 뒤에 있되, skip에 겹치지 않도록 중간에 반복문을 통해 올바른 idx 값 찾아주기
        for _ in range(index):
            idx += 1
            while alphabet[idx % len(alphabet)] in list(skip):
                idx += 1
        
        # alphabet의 길이를 넘어갈 수도 있기 때문에 %를 통해 범위 내의 index를 취해주기
        answer += alphabet[idx % len(alphabet)]
        
    return answer