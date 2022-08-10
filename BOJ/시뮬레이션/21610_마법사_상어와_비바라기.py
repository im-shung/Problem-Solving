from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
A = [[0] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    A[i][1:] = list(map(int,input().split()))
move = [[0] * 2 for _ in range(m+1)]
for i in range(1,m+1):
    move[i] = list(map(int,input().split()))
d = [(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)] # 1번부터 8번까지 8개의 방향 
cloud = deque([(n,1),(n,2),(n-1,1),(n-1,2)]) # 구름 위치

c = 1 # 구름 이동한 횟수  
while c <= m:
    # 1. 모든 구름이 di 방향으로 si칸 이동한다.
    for _ in range(len(cloud)):
        x,y = cloud.popleft()
        _x, _y = d[move[c][0]]
        xx, yy = x + _x* move[c][1], y + _y* move[c][1]
        while True:
            if xx < 1: xx += n
            elif xx > n: xx -= n
            else: break
        while True:
            if yy < 1: yy += n
            elif yy > n: yy -= n
            else: break
        cloud.append((xx,yy))
    # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
        A[xx][yy] += 1 
    # 3. 구름이 모두 사라진다.
    # 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 
    # 물복사버그 마법을 사용하면, 
    # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    for x,y in cloud:
        cnt = 0
        for i in (2,4,6,8):
            _x, _y = d[i]
            xx, yy = x + _x, y + _y
            if 1 <= xx <= n and 1 <= yy <= n:
                if A[xx][yy] != 0:
                    cnt += 1
        A[x][y] += cnt
    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 
    # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    new_cloud = deque()
    for i in range(1,n+1):
        for j in range(1,n+1):
            if not (i,j) in cloud and A[i][j] >= 2:
                new_cloud.append((i,j))
                A[i][j] -= 2
    cloud = new_cloud
    c += 1
sum = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        sum += A[i][j]
print(sum)