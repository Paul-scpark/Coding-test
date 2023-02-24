# 코딩 테스트 연습문제 - python

### 체감 난이도: 1
### for & range 함수 활용, indexing
### https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    
    answer, t_len = 0, len(p)
    # index 0부터 부분 문자열을 만들 수 있는 범위까지 range로 설정
    for i in range(0, len(t) - t_len + 1):
        # 주어진 p의 길이만큼 부분 문자열 (subset)을 만듦
        subset = t[i:i + t_len]
        
        # subset과 p 값을 비교
        if int(subset) <= int(p): answer += 1
            
    return answer