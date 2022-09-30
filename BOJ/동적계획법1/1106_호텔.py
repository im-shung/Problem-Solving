INF = (1e9)
c, n = map(int,input().split())
info = [tuple(map(int,input().split())) for _ in range(n)]
dp = [0] + [INF] * (c + 100)

for cost, customer in info:
    for i in range(customer, c + 101):
        dp[i] = min(dp[i], dp[i - customer] + cost)
print(min(dp[c:]))
