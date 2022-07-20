# SW Expert Academy 
# 5097. [파이썬 S/W 문제해결 기본 - Queue] 6일차 - 회전 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg

# import sys
# sys.stdin = open("../sample_input.txt", "r")


import queue

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = queue.Queue()
    for i in arr:
        q.put(i)
    for i in range(M%N):
        q.put(q.get())
        
    print(f"#{test_case} {q.get()}")