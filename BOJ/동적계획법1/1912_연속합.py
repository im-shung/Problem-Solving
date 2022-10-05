INF = -(1e9)
n = int(input())
s = [0] + list(map(int, input().split()))
dp = [INF] * (n + 1)
dp[1] = s[1]
for i in range(1, n + 1):
    dp[i] = max(s[i], dp[i - 1] + s[i]) # 현재 값 vs 이전 값 + 현재 값
print(max(dp))