import sys
input = sys.stdin.readline


n = int(input())
dp = [0] * (n + 1) 
dp[0], dp[1] = 0, 0

for i in range(2, n+1):
    min_value = 1e9
    if i % 3 == 0:
        min_value = min(min_value, dp[i//3])
    if i % 2 == 0: # 6처럼 2로도 나눠지고, 3로도 나눠지는 수가 있기에 if-elif문을 쓰면 안된다.
        min_value = min(min_value, dp[i//2])
    min_value = min(min_value, dp[i-1])
    dp[i] = min_value + 1
print(dp[n])