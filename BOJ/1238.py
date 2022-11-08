import sys
import heapq
input = sys.stdin.readline

INF = 1e9

def search(start, graph, distance):
    Q = []
    heapq.heappush(Q, [0, start])
    distance[start] = 0
    while Q:
        d, v = heapq.heappop(Q)
        if distance[v] < d:
            continue
        for next_dist, next_v in graph[v]:
            dist = distance[v] + next_dist
            if dist < distance[next_v]:
                distance[next_v] = dist
                heapq.heappush(Q, [dist, next_v])

    return distance[X]

if __name__ == '__main__':
    N, M, X = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    graph_r = [[] for _ in range(N + 1)]

    distance = [INF for _ in range(N + 1)]
    distance_r = [INF for _ in range(N + 1)]

    for _ in range(M):
        s, e, dist = map(int, input().split())
        graph[s].append([dist, e])
        graph_r[e].append([dist, s])

    search(X, graph, distance)
    search(X, graph_r, distance_r)

    max_dist = 0
    for v in range(1, N + 1):
        max_dist = max(max_dist, distance[v] + distance_r[v])

    print(max_dist)