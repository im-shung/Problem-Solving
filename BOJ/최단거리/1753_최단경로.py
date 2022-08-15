import heapq
import sys

n,e = map(int,input().split())
start = int(input())
INF = sys.maxsize
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

def dijkstra(start):
    Q = []
    heapq.heappush(Q,(0,start))
    distance[start] = 0
    
    while Q:
        w,v = heapq.heappop(Q)
        if distance[v] < w:
            continue
        for next,value in graph[v]:
            cost = distance[v] + value
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(Q,(cost,next))
for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w)) 
dijkstra(start)                
for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:print(distance[i])