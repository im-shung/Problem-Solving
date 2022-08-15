import heapq

def dijkstra(start):
    Q = []
    heapq.heappush(Q,(0,start))
    distance[start] = 0
    while Q:
        dist,now = heapq.heappop(Q)
         # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
        if distance[now] < dist:
            continue
        # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
        for next,value in graph[now]:
            cost = distance[now] + value
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(Q,(cost,next))
n,m,k,x = map(int,input().split())

INF = (1e9)
graph = [[] for _ in range(n+1)] 
visited = [False] * (n+1)
distance = [INF] * (n+1)
for _ in range(m):
    A,B = map(int,input().split())
    graph[A].append((B,1))
dijkstra(x)
cnt = 0
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        cnt += 1
if cnt == 0: print(-1)