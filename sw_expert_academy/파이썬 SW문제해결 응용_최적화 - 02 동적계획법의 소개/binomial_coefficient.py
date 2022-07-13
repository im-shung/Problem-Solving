# SW Expert Academy 
# 5256. [파이썬 S/W 문제해결 최적화] 2일차 - 이항계수 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYNNbK29EDFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")

# DP문제 - 메모이제이션으로 풀지 않으면 시간초과
def binomial_coefficient(n,k):
    for i in range(n+1):
            for j in range(min(i, k) + 1):
                if j == 0 or j == i:
                    B[i][j] = 1
                else:
                    B[i][j] = B[i-1][j-1] + B[i-1][j] # nCk = n-1Ck + n-1Ck-1
    return B[n][k]

for test_case in range(1, int(input())+1):
    n, a, b = map(int, input().split())
    B = [[0 for _ in range(n+1)] for _ in range(n+1)]
    print(f"#{test_case} {binomial_coefficient(n,a)}")