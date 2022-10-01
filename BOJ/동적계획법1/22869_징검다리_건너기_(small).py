import sys
sys.stdin = open("sample_input.txt", "r")

n, k = map(int,input().split())
rock = [0] + list(map(int,input().split()))
dp = [-1] * (n + 1)
dp[1] = 1

for i in range(1, n + 1):
    if dp[i] == -1: continue # 건너갈 수 없는 칸
    for j in range(i + 1, n + 1):
        power = (j - i) * (1 + abs(rock[i] - rock[j]))
        if power <= k:
            dp[j] = 1
    if dp[n] == 1:
        print("YES")
        exit()
print("NO")