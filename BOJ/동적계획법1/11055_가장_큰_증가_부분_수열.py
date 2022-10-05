n = int(input())
s = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1):
    flag = True
    for j in range(i):
        if s[i] > s[j]:
            flag = False
            dp[i] = max(dp[i], dp[j] + s[i])
    if flag:
        dp[i] = s[i]
print(max(dp))