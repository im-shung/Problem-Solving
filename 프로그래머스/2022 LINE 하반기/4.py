from collections import deque

# 격자형 최소거리 --> BFS 택 
# 용암, 산, 돌 얘기

wall= ["H.H",".HX","H.H"]	
# result = [[2,0,-1],[0,2,0],[1,0,-1]]

n = len(wall)
m = len(wall[0])

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def possible(si, sj, ei, ej, i1, j1, i2, j2):
    i1, i2 = min(i1,i2), max(i1,i2)
    j1, j2 = min(j1,j2), max(j1,j2)
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            if not in_range(i, j):
                return False
            if (i,j) in [(si, sj), (ei, ej)]:
                if wall[i][j] != 'H':
                    return False
            else:
                if wall[i][j] != '.':
                    return False
    return True
            
dist = [[-1 for _ in range(m)] for _ in range(n)]
Q = deque()
Q.append((n - 1, 0))
dist[n-1][0] = 1

while Q:
    i, j = Q.popleft()
    
    # 인접
    for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
        ni, nj = i + di, j + dj
        if not in_range(ni, nj) or wall[ni][nj] != 'H' or dist[ni][nj] != -1:
            continue
        dist[ni][nj] = dist[i][j] + 1
        Q.append((ni, nj))

    # 두 칸 위
    if possible(i, j, i - 2, j, i, j, i - 2, j) and dist[i - 2][j] == -1:
        dist[i - 2][j] = dist[i][j] + 1
        Q.append((i - 2, j))
    
    # 좌우
    for d in [-3, -2, 2, 3]:
        if possible(i, j, i, j + d, i - 1, j, i, j + d) and dist[i][j + d] == -1:
            dist[i][j + d] = dist[i][j] + 1
            Q.append((i, j + d))
    
    # 대각선
    for d in [-1, 1]:
        if possible(i, j, i - 1, j + d, i - 1, j, i, j + d) and dist[i - 1][j + d] == -1:
            dist[i - 1][j + d] = dist[i][j] + 1
            Q.append((i - 1, j + d))

for i in range(n):
    for j in range(m):
        if wall[i][j] in '.X':
            print(0, end = ' ')
        else:
            print(dist[i][j], end = ' ')
    print()