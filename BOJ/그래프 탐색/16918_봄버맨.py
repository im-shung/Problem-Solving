from collections import deque
import sys
input = sys.stdin.readline

moves = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs():
    global time, Q, n
    while time < n:
        time += 1
        if time == n: return
        while Q: # 2초 후
            i,j = Q.popleft() 
            map[i][j] = '.' 
            for _x, _y in moves:
                dx = i + _x
                dy = j + _y
                if -1 < dx < r and -1 < dy < c:
                    map[dx][dy] = '.'
        time += 1
        if time == n: return
        for i in range(r): # 3초 후
            for j in range(c):
                if map[i][j] == 'O':
                    Q.append((i,j))
                else:
                    map[i][j] = 'O' 
                    
r,c,n = map(int,input().split())
map = [list(input().strip()) for _ in range(r)] # 0초
time = 1 # 1초 후
Q = deque()
if n > 1:
    for i in range(r):
        for j in range(c):
            if map[i][j] == 'O':
                Q.append((i,j))
            else:
                map[i][j] = 'O' 
    if n > 2:
        bfs()
for i in range(r):
    print(''.join(map[i]))