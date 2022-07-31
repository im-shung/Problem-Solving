import sys
input = sys.stdin.readline

def dp(change):
    for i in coin:
        for n in range(1,change+1):
            if n >= i: # 금액이 동전보다 클 때 
                memo[n] += memo[n-i]
    return memo[change]

for _ in range(int(input())):
    n = int(input()) 
    coin = list(map(int,input().split()))
    change = int(input()) 
    memo = [0] * (change +1)
    memo[0] = 1 # 중요
    print(dp(change))