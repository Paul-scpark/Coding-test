# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### for loop의 enumerate, list와 dictionary 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    
    dic, answer_lst = {}, []
    # strings에서 n번째 인덱스를 key로 하고 단어를 value로 하는 dict 생성
    for idx, word in enumerate(strings):
        # 동일한 key가 있는 경우에는 list 내에서 append
        if word[n] in dic.keys():
            dic[word[n]].append(word)
        else: 
            dic[word[n]] = [word]
    
    # 위에서 만든 dict에서 key 값을 기준으로 정렬하여 answer_lst에 추가
    for key in sorted(list(dic.keys())):
        answer_lst += sorted(dic[key])
    
    return answer_lst