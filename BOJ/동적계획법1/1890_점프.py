n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] > 0:
            for _x, _y in [(0,1),(1,0)]:
                dx, dy = i + _x * matrix[i][j], j + _y * matrix[i][j]
                if 0 <= dx < n and 0 <= dy < n:
                    if i == dx and j == dy: break
                    dp[dx][dy] += dp[i][j] 
print(dp[-1][-1])
            

# 시간 초과 
# n = int(input())
# matrix = [list(map(int,input().split())) for _ in range(n)]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp[0][0] = 1

# Q = deque()
# Q.append((0,0))

# while Q:
#     i, j = Q.popleft()
#     for _x, _y in [(0,1),(1,0)]:
#         dx, dy = i + _x * matrix[i][j], j + _y * matrix[i][j]
#         if 0 <= dx < n and 0 <= dy < n:
#             if i == dx and j == dy: break
#             Q.append((dx, dy))
#             dp[dx][dy] += dp[i][j]
            
# print(dp[-1][-1])
