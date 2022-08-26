# 2022 KAKAO TECH INTERNSHIP - python

### 체감 난이도: 2
### 리스트 및 딕셔너리 자료 구조 활용, zip 함수 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3

def solution(survey, choices):
    
    # 미리 같은 유형 내에서 사전 순서대로 정렬 (RT, CF, JM, AN)
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0,
           'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # 각 설문 항목에 대해 점수가 높은 항목의 유형으로 점수 채워주기
    for key, value in zip(survey, choices):
        if value <= 3: dic[key[0]] += 4 - value
        elif value >= 5: dic[key[1]] += value - 4
    
    # RT, CF, JM, AN 유형 중에서 어떤 항목이 더 컸는지 확인하여 최종 결과 도출
    i = 0 ; answer = ''
    key_lst = list(dic.keys())
    while True:
        if i == len(key_lst): break
        
        # 미리 사전 순서로 정렬해놓았으니, 같은 항목이면 더 빠른 인덱스 값을 반환
        if dic[key_lst[i]] >= dic[key_lst[i + 1]]: answer += key_lst[i]
        else: answer += key_lst[i + 1]
        i += 2
        
    return answer
