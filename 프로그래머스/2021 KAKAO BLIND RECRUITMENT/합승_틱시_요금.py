import heapq
def solution(n, s, a, b, fares):
    INF = (10**6)
    graph = [[] for _ in range(n+1)]
    for x,y,d in fares:
        graph[x].append((d,y))
        graph[y].append((d,x))

    def dijkstra(start,end):
        distance = [INF] * (n+1)
        distance[start] = 0
        Q = [[0,start]]

        while Q:
            cost,node = heapq.heappop(Q)

            if distance[node] < cost: continue

            for c,_n in graph[node]:
                c += cost
                if c < distance[_n]:
                    distance[_n] = c
                    heapq.heappush(Q,[c,_n])
        return distance[end]
    cost = INF
    # ! 생각 못했던 부분
    # 합승 구간 고려하기
    for i in range(1,n+1):
        cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    return cost