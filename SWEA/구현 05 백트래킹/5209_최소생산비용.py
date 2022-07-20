# SW Expert Academy 
# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYGf7K180DFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")      

T = int(input())

def back_tracking(c,r,sum): 
    global min,stack
    if c == N: 
        if min > sum: min = sum
        return
    if min < sum: return
    for i in range(N):
        if not i in stack:
            stack.append(i)
            back_tracking(c+1,i,sum+V[c][i]) 
            stack.pop()

for test_case in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)] 
    min = 987654321
    stack = list()
    back_tracking(0,0,0)
    print("#"+str(test_case),min)        