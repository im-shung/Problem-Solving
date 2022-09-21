import sys
input = sys.stdin.readline

MAX = 201
dp = [[0]*MAX for i in range(MAX)] # dp[k][n]

n,k = map(int,input().split())

for i in range(MAX):
    dp[1][i] = 1 # k가 1이면 경우의 수는 1
    dp[2][i] = i+1 # k가 2이면 경우의 수는 n+1

for i in range(2,MAX):
    dp[i][1] = i
    for j in range(2,MAX):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j])% 1_000_000_000
print(dp[k][n])