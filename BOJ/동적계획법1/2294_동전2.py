INF = (1e9)

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [INF for _ in range(k + 1)]
dp[0] = 0
for i in range(1, k + 1):
    for coin in coins:
        if i % coin == 0:
            dp[i] = min(dp[i], i//coin)
        else:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])