import sys,math
input = sys.stdin.readline


n = int(input())
dp = [0] * (n + 1) # n을 표현하기 위해 필요한 최소 숫자의 개수
dp[0], dp[1] = 0, 1

for i in range(2, n+1):
    min_value = 1e9
    for j in range(1, int(math.sqrt(i)) + 1): # math.sqrt(i): i의 제곱근 구하기 
        min_value = min(min_value, dp[i - j ** 2])
    dp[i] = min_value + 1
print(dp[n])