import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
coins = []
dp = [0 for _ in range(T+1)] # dp[n]: 금액 n에 대한 동전 교환 방법의 가짓수
dp[0] = 1 # 아무 동전도 사용하지 않는 경우

for _ in range(k):
    p, n = map(int,input().split())
    coins.append((p,n))

for coin, cnt in coins:
    for money in range(T,0,-1): # T원부터 1원까지 내려가며 진행
        for i in range(1,cnt+1): # 현재 동전 coin의 개수만큼 for문 진행
            if money-coin*i >= 0: # 0원 이상인 경우
                dp[money] += dp[money-coin*i]
print(dp[T])