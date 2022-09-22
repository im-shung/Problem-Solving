import sys
sys.stdin = open("sample_input.txt", "r")

WEIGHT = 0
VALUE = 1

for t in range(int(input())):
    n, m = map(int,input().split()) # 박스의 크기 n, 상품의 개수 m
    
    item = [[0,0]]
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for _ in range(m):
        s,p = map(int,input().split()) # 상품의 크기 s, 상품의 가격 p
        item.append([s,p])
    
    for k in range(1,m+1):
        for w in range(1,n+1): # 최대 무게를 하나씩 올려가면서 계산
            if item[k][WEIGHT] <= w: # 이전 최대가치를 사용하는 것보다 이전걸 빼고 현재물건을 넣는게 더 좋다면 넣어주자
                dp[k][w] = max(dp[k - 1][w], item[k][VALUE] + dp[k - 1][w - item[k][WEIGHT]])
            else:
               dp[k][w] = dp[k-1][w] # 아니라면 이전가치를 그대로 사용
    
    print(f"#{t+1} {dp[m][n]}")