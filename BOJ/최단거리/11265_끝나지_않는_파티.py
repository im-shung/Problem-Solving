import heapq
import sys
sys.stdin = open("sample_input.txt", "r")

n,m = map(int,input().split())

def dijkstra(start):
    Q = []
    heapq.heappush(Q,(0,start))
    distance = distance2[start]
    distance[start] = 0
    while Q:
        w, v = heapq.heappop(Q)
        if distance[v] < w:
            continue
        for next,value in graph[v]:
            cost = distance[v] + value
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(Q,(cost,next))
graph = [[] for _ in range(n+1)]
INF = sys.maxsize
for i in range(1,n+1):
    s = list(map(int,input().split()))
    for j in range(n):
        if s[j] != 0:
            graph[i].append((j+1,s[j]))
distance2 = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dijkstra(i)
for _ in range(m):
    start,end,time = map(int,input().split())
    result = distance2[start][end]
    if result > time:
        print("Stay here")
    else:
        print("Enjoy other party")