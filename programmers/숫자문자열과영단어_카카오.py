# 2021 카카오 채용연계형 인턴십 - python

### 체감 난이도: 3
### 숫자를 확인하는 isdigit 함수, list와 dic 활용, replace 함수 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    
    # 주어진 숫자와 영단어를 dic 형태로 정의
    dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
           'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    idx = 0
    text, answer = '', ''
    while idx != len(s):
        
        text += s[idx]
        
        # 한 단어씩 계속 붙여나가는 text가 dic의 keys 값에 존재하는지 확인
        # 만약 존재한다면, keys에 맞는 value로 변환하여 answer에 추가하고, text 초기화
        if text in list(dic.keys()):
            answer += str(dic[text])
            text = text.replace(text, '')
            
        # 현재 text가 숫자 (isdigit) 라면, 바로 answer에 추가하고, text 초기화
        elif text.isdigit():
            answer += str(text)
            text = text.replace(text, '')
        
        idx += 1
    
    return int(answer)