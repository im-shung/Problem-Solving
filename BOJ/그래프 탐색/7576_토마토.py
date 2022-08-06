from collections import deque
import sys
input = sys.stdin.readline

moves = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs():
    global Q, day
    cnt = 0
    while Q:
        i, j, cnt = Q.popleft()
        day = cnt
        cnt += 1
        for _x, _y in moves:
            dx = i + _x
            dy = j + _y
            if -1 < dx < n and -1 < dy < m:
                if tomato[dx][dy] == '0':
                    tomato[dx][dy] = '1'
                    Q.append((dx,dy,cnt))   

m, n = map(int,input().split())
tomato = [list(input().split()) for _ in range(n)]
Q = deque()
flag = 0; day = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == '1':
            Q.append((i,j,0))
        elif tomato[i][j] == '0':
            flag = 1

if flag == 0: # 모든 토마토가 익어 있는 상황
    print(0)
else:
    bfs()
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == '0':
                flag = 0
    if flag == 0:
        print(-1)
    else:
        print(day)