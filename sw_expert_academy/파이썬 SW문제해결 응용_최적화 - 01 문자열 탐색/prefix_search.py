# SW Expert Academy 
# 5253. [파이썬 S/W 문제해결 최적화] 1일차 - 접두어 검색 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYM1Ca240DFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    prefix = set(); cnt = 0
    for i in range(N): 
        A = input()
        for j in range(1,len(A)+1):
            prefix.add(A[:j])
    for i in range(M): 
        B = input()
        if B in prefix:
            cnt += 1
    print(f"#{test_case} {cnt}")