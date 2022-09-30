n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1 # 0원짜리 

for coin in coins:
    for money in range(coin,k + 1): # 동전이 3원짜리라면 dp[1],dp[2]는 고려할 필요가 없으므로 dp[3]부터 순회한다.
        if money - coin >= 0:
            dp[money] += dp[money - coin]
print(dp[k])