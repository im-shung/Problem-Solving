import sys
input = sys.stdin.readline # input이 sys.stdin.readline의 속도를 갖는다.

n,m = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = area[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(int(input())):
    x, y, i, j = map(int,input().split())
    print(dp[i][j] - dp[x-1][j] - dp[i][y-1] + dp[x-1][y-1])