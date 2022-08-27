# 2022 KAKAO BLIND RECRUITMENT - python

### 체감 난이도: 3
### 조건에 따른 무한루프 while문
### https://school.programmers.co.kr/learn/courses/30/lessons/60057

# 같은 문자열이 최대 몇 번 나오는지에 따라서, 반복된 횟수와 문자열을 붙여주는 함수
def find_answer(count, prev, answer):
    
    if count == 1: answer += str(prev)
    else: answer += str(count) + str(prev)
    return answer

def solution(s):
    
    # 1. [기본 조건] 문자열을 자를 수 있는 최댓값은 s의 길이
    answer_lst = []
    for max_len in range(1, len(s)):    
        idx, count = 0, 1
        prev, answer = '', ''
        
        # 2. 주어진 압축 단위에 맞게 반복해서 단어들을 쪼개기. 가장 마지막 단어가 나올 때까지 반복
        while True:
            if idx + max_len > len(s):
                now = s[idx:]
                break
            else: now = s[idx:idx + max_len]
            
            # 3-1. 저번에 나온 것과 이번에 나온 것을 비교해서 나온 횟수만큼 더해주기
            if now == prev: count += 1
            # 3-2. 저번에 나온 것과 이번에 나온 것이 다르다면, '나온 횟수 + 문자열'로 answer 할당해주고, count 초기화
            else: 
                if prev != '': 
                    answer = find_answer(count, prev, answer)
                count = 1
            
            prev = now      # 다음 루프에서 비교하기 위해 이번 단어를 prev로 할당
            idx += max_len  # max_len 만큼 주어진 단어를 인덱싱하기 위해 idx 값 수정
        
        # 3-3. 가장 마지막 루프에서 나온 결과에 대해서도 answer에 추가
        answer = find_answer(count, prev, answer)
        
        # 4. 문자열이 압축 단위와 맞지 않아서 잘린 경우에는 answer의 마지막에 그대로 붙여주기
        if now != '': 
            answer += str(now)
        answer_lst.append(len(answer))
    
    # 5. 모든 조건에서 가장 길이가 짧게 자른 케이스의 길이를 return. Input 문자열이 1개 일때, 예외 처리
    if len(answer_lst) != 0:
        return min(answer_lst)
    return 1