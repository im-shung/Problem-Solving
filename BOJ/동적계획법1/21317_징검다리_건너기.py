from sys import stdin
input = stdin.readline

SMALL = 0
BIG = 1
INF = (1e9)

n = int(input())
jump = [(INF,INF)] + [tuple(map(int,input().split())) for _ in range(n-1)] # 1돌부터 n-1돌 점프 
k = int(input())

if n == 1:
    print(0)
    exit()
    
dp = [0] + [0] + [jump[1][0]] + [INF] * (n-2) # 0돌부터 n돌까지 거리

# 작은 점프, 큰 점프로만 dp 구하기 
for i in range(3, n + 1):
    dp[i] = min(dp[i - 1] + jump[i - 1][SMALL], dp[i - 2] + jump[i - 2][BIG])

# 매우 큰 점프 적용해보기
mn = dp[-1] # !!!!!! 변수명에 max, min x
for j in range(1,n-2):
    dp2 = dp[:]
    if dp2[j] + k < dp2[j + 3]:
        dp2[j + 3] = dp2[j] + k
        for i in range(j + 4, n+1): # !!!!! n이 아니라 n+1  ^ㅁ^;;
           dp2[i] = min(dp2[i - 1] + jump[i - 1][SMALL], dp2[i - 2] + jump[i - 2][BIG])
        if mn > dp2[-1]:
            mn = dp2[-1]
print(mn)