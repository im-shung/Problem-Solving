import sys
sys.setrecursionlimit(10**9) # !!런타임 에러 해결: 최대 재귀 깊이 늘리기!!
N = int(sys.stdin.readline().strip())
parent = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(N-1):
    n1, n2 = map(int,sys.stdin.readline().split())
    parent[n1].append(n2)
    parent[n2].append(n1)
def dfs(s):
    for i in parent[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)     
dfs(1)       
print('\n'.join(map(str,visited[2:])))