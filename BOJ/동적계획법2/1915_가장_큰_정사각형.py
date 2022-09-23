# 45퍼에서 틀림 

import sys
# input = sys.stdin.readline
sys.stdin = open("sample_input.txt", "r")

n,m = map(int,input().split())

matrix = [list(map(int,input())) for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

MIN = min(n,m)

for i in range(n+1):
    print(dp[i])

max = 0
zero_check = False
for x in range(MIN-1,0,-1):
    for i in range(1,n+1):
        for j in range(1,m+1):
            a, b = i+x, j+x
            if 1 <= a <= n and 1 <= b <= m:
                val = dp[a][b] - dp[a][j-1] - dp[i-1][b] + dp[i-1][j-1]
                if val == 1: 
                    zero_check = True
                elif max > val:
                    continue
                elif val == (x+1)**2:
                    max = (x+1)**2
                    continue
if max == 0:
    if zero_check:
        max = 1
print(max)
    