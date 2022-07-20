# SW Expert Academy 
# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYGf7K180DFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")      

T = int(input())

def back_tracking(now,cnt):
    global result
    
    if now == N-1: 
        if result > cnt:
            result = cnt
        return
    
    if result < cnt: 
        return 
    cnt += 1
    for i in range(arr[now],0,-1):
        if now+i <= N-1:
            back_tracking(now+i,cnt)       

for test_case in range(1, T + 1):
    N, *arr = map(int, input().split())
    result = 987654321
    back_tracking(0,-1)
    print("#"+str(test_case),result)