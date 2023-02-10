from collections import defaultdict
import sys
input = sys.stdin.readline

n, w = map(int,input().split())
graph = defaultdict(int)
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u] += 1
    graph[v] += 1

leaf = 0 # 리프노드 갯수
for idx in range(2,n+1):
    if graph[idx] == 1:
        leaf += 1
print(w/leaf)
