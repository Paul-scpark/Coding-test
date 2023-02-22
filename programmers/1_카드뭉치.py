# 코딩 테스트 연습문제 - python

### 체감 난이도: 1
### list comprehension, indexing
### https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    
    # 주어진 조건에 따라, 카드는 중복하지 않고 한 장만 사용
    # 또한 카드를 사용하지 않고 다음 카드로 갈 수 없으며, 순서를 바꿀 수 없음
    # 따라서 goal에서 나온 순서를 그대로 살려서 각각 cards1과 cards2에서 겹치는 항목들 추리기
    cards1_union = [ _ for _ in goal if _ in cards1 ]
    cards2_union = [ _ for _ in goal if _ in cards2 ]
    
    # 카드를 사용하지 않고 다음 카드로 넘어갈 수는 없지만, cards1이나 cards2의 단어가 더 많이 나온 경우가 존재
    # 따라서 goal에서 나온 길이만큼만 추려서 일치하는지 여부를 파악하면, 단어 생성 여부를 결정할 수 있음
    if (cards1[0:len(cards1_union)] == cards1_union) & (cards2[0:len(cards2_union)] == cards2_union):
        return "Yes"
    return "No"