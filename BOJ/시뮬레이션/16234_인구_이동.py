from collections import deque
import sys
input = sys.stdin.readline

n,l,r = map(int,input().strip().split())
graph = [list(map(int,input().strip().split())) for _ in range(n)]

moves = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(i,j):
    Q = deque([(i,j)])
    visited[i][j] = True
    union = [(i,j)]
    sum = graph[i][j]
    
    while Q:
        x,y = Q.popleft()
        for _x,_y in moves:
            xx = x +_x
            yy = y + _y
            if 0 <= xx < n and 0 <= yy < n :
                if not visited[xx][yy]:
                    if l <= abs(graph[x][y]-graph[xx][yy]) <= r:
                        visited[xx][yy] = True
                        Q.append((xx,yy))
                        union.append((xx,yy))
                        sum += graph[xx][yy]
    new = sum//len(union)
    for x,y in union:
        graph[x][y] = new
    return len(union)

day = 0
moving = True
while True:
    moving = False
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i,j) > 1:
                    moving = True
    if not moving: break
    day += 1
print(day)