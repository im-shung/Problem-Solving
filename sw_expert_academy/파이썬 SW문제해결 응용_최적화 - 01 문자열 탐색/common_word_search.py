# SW Expert Academy 
# 5252. [파이썬 S/W 문제해결 최적화] 1일차 - 공통 단어 검색 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYM1Ca240DFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = []; cnt = 0
    for i in range(N): A.append(input())
    for i in range(M): 
        if input() in A:
            cnt += 1
    print(f"#{test_case} {cnt}")