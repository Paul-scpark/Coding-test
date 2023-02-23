# 코딩 테스트 연습문제 - python

### 체감 난이도: 1
### enumerate, dic 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    
    # s의 문자 하나와 그에 따른 index를 확인하여 answer를 return
    dic, answer = {}, []
    
    for idx, i in enumerate(s):
        # 과거에 나온 적이 없었다면, dic의 key = i, value = idx로 설정하고, answer -1를 추가
        if i not in dic.keys():
            dic[i] = idx
            answer.append(-1)
        
        # 과거에 나왔다면, 현재의 idx 위치와 그 전의 위치를 담고 있는 dic[i]를 통해 몇 칸 앞에 존재하는지 확인
        # 그리고 이 과정에서 해당 문자 (i)의 value 값을 갱신시켜주기
        else:
            answer.append(idx - dic[i])
            dic[i] = idx
            
    return answer