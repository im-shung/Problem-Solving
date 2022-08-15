from collections import deque
n,m = map(int,input().split())

def sort():
    Q = deque()
    result = [0] * (n+1)
    for i in range(1,n+1):
        if indegree[i] == 0:
            Q.append(i)
    while Q:
        x = Q.popleft()
        result[x] += 1
        for i in graph[x]:
            indegree[i] -= 1
            result[i] = result[x]
            if indegree[i] == 0:
                Q.append(i)
    for i in range(1,n+1):
        print(result[i], end=' ')

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1
sort()