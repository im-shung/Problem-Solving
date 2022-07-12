# SW Expert Academy 
# 5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ1r6qfkDFAWg

import sys
sys.stdin = open("../sample_input.txt", "r")

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split()) # 수열의 길이 N, 수열 개수 M
    sequences = [list(map(int, input().split())) for _ in range(M)]
    S = sequences[0]
    for i in range(1, M):
        D = sequences[i]
        for j in range(len(S)):
            if S[j] > D[0]:
                S[j:j] = D
                break
        else: S.extend(D)
    S.reverse()
    print(f"#{test_case} {' '.join(map(str,S[:10]))}")