n = int(input())
memo = [[0 for _ in range(30)] for _ in range(30)]
def dp(n,k):
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j == 0 or j == i:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
    return memo[n][k]        
for _ in range(n):
    k,n = map(int,input().split())
    print(dp(n,k))