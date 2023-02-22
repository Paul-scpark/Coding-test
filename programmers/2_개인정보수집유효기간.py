# 2023 Kakao Blind Recruitment - python

### 체감 난이도: 2
### list, dict 활용, 정상적인 날짜로 값을 변환
### https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3

def solution(today, terms, privacies):
    
    # terms 정보를 담고 있는 dict = {term 이름: term 기간} 형태
    today_date = int(today.replace('.', ''))
    terms_dic = { i.split()[0]: int(i.split()[1]) for i in terms }
    
    answer_lst = []
    for idx, i in enumerate(privacies):
        # 개인정보 수집 일자 (date, y & m & d)와 약관 종류 (term) 정의
        date, term = i.split()
        y, m, d = list(map(int, date.split('.')))
        
        # y & m & d의 값에 유효기간을 반영하고, 그 날짜가 정상적이도록 전처리
        m += terms_dic[term] ; d -= 1
        while True: # m과 d가 정상적인 날짜 값이 될 수 있을 때까지 반복
            if (m >= 1 and m <= 12) and (d >= 1 and d <= 28): break # 탈출 조건
            if d == 0: d = 28 ; m -= 1
            if m == 0: m = 12 ; y -= 1
            if m > 12: m -= 12 ; y += 1
        
        # 현재 날짜 (today_date)와 만료 날짜 (exp_date)를 비교
        exp_date = int( str(y) + str(m).zfill(2) + str(d).zfill(2) )
        
        if today_date > exp_date: answer_lst.append(idx + 1)
            
    return answer_lst