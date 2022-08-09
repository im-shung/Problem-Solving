# PyPy3로 제출해야 시간 초과 X
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    Q = deque([v])
    cnt = 1
    visited = [False] * (n+1)
    visited[v] = True
    while Q:
        x = Q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                Q.append(i)
                cnt += 1
    return cnt

n,m = map(int,input().split())
graph  = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)
result = []
for i in range(1, n+1): # !! 기억해야 하는 dfs 포인트
    result.append(bfs(i))
max = max(result)
for i in range(len(result)):
    if max == result[i]:
        print(i+1, end=' ')