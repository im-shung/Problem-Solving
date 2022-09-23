# 복습 필요

n,m,h = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [0 for _ in range(h+1)]

for row in matrix:
    for i in range(h,0,-1): # 누적합은 뒤에서부터 쌓아줘야 중복이 안 생김
        if not dp[i]: # 0이라면 패스 
            continue
        for col in row:
            if i + col > h:
                continue
            dp[i+col] += dp[i]
    for col in row:
        dp[col] += 1
        
print(dp[h]%10007)