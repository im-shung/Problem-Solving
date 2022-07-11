# SW Expert Academy 
# 5254. [파이썬 S/W 문제해결 최적화] 1일차 - 부분 문자열 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYM1Ca240DFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N, string = input().split()
    N = int(N)
    prefix = set()
    s = len(string)
    for i in range(0,s): 
        for j in range(i+1,s+1):
            prefix.add(string[i:j])
    prefix = list(prefix)
    prefix.sort()
    print(f"#{test_case} {prefix[N-1][0]} {len(prefix[N-1])}")