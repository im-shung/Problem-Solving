# SW Expert Academy 
# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg

import sys
sys.stdin = open("../sample_input.txt", "r")

T = int(input())

# 이긴 경우
win = [(1,3), (2,1), (3,2)]

# 그룹 나누기
def divide(group):
    # 그룹이 1명일 때 
    if len(group) == 1:
        return group

    # mid를 중심으로 두 그룹으로 나눈다. 
    ### 분할정복 알고리즘 사용 ###
    mid = (len(group) -1)//2+1
    front = group[:mid]
    rear = group[mid:]
    
    front = divide(front)
    rear = divide(rear)
    
    return game(front[0], rear[0])
    
# 그룹 내에서 가위바위보 진행    
def game(f, r):
    if cards[f] == cards[r]: 
        return [f]
    for idx in range(3):
        a, b = win[idx]
        if a == cards[f] and b == cards[r]:
            return [f]
        elif a == cards[r] and b == cards[f]:
            return [r]   

for test_case in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split())) # 1: 가위, 2: 바위, 3: 보
    groups = list(range(N))

    print(f"#{test_case} {divide(groups).pop()+1}")
