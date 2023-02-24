# 프로그래머스 코딩테스트 연습문제 - python

### 체감 난이도: 2
### for문과 if문 활용, dictionary 활용
### https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    alphabet_dic = {
        "zero": 0, 
        "one": 1, 
        "two": 2, 
        "three": 3,
        "four": 4, 
        "five": 5, 
        "six": 6, 
        "seven": 7, 
        "eight": 8, 
        "nine": 9    
    }
    
    temp, answer = '', ''
    for i in numbers:
        temp += i
        if temp in alphabet_dic.keys():
            answer += str(alphabet_dic[temp])
            temp = ''
            
    return int(answer)