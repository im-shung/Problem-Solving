from _collections import deque

def dfs(x):
    visited[x] = True
    print(x, end = " ")
    for y in graph[x]:
        if not visited[y]:
            dfs(y)

def bfs(x):
    Q = deque()
    Q.append(x)
    visited[x] = True
    while Q:
        x = Q.popleft()
        print(x, end=" ")
        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                Q.append(y)

if __name__ == '__main__':
    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for _ in range(1, N + 1):
        graph[_].sort()

    visited = [False for _ in range(N + 1)]
    dfs(V)
    print()
    visited = [False for _ in range(N + 1)]
    bfs(V)