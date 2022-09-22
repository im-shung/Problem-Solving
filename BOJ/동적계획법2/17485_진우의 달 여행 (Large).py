import sys
# input = sys.stdin.readline
sys.stdin = open("sample_input.txt", "r")

INF = 1e9

RIGHT = 0
MID = 1
LEFT = 2

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0,0,0] for _ in range(m)]] + [[[INF,INF,INF] for _ in range(m)] for _ in range(n)]

for i in range(1,n+1):
    for j in range(m):
        if j < m-1: # RIGHT에서 온 값
            dp[i][j][RIGHT] = min(dp[i-1][j+1][MID],dp[i-1][j+1][LEFT]) + matrix[i-1][j]
        if 0 < j: # LEFT에서 온 값
            dp[i][j][LEFT] = min(dp[i-1][j-1][MID],dp[i-1][j-1][RIGHT]) + matrix[i-1][j]
        # MID에서 온 값
        dp[i][j][MID] = min(dp[i-1][j][RIGHT],dp[i-1][j][LEFT]) + matrix[i-1][j]

min_value = INF
for row in dp[i]:
    for each in row:
        min_value = min(min_value,each)
print(min_value)
