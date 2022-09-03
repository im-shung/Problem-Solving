import sys
sys.stdin = open("sample_input.txt", "r")

input = sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input().strip()) for _ in range(n)]

idx = n-1
cnt = 0
for i,coin in enumerate(coins):
    if coin > k:
        idx = i-1
        break
while k > 0:
    if k >= coins[idx]:
        cnt += k//coins[idx]
        k -= k//coins[idx]*coins[idx]
    idx -= 1
print(cnt)   