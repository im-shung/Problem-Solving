import sys
sys.stdin = open("C:\Program_study\AlgorithmStudy\sample_input.txt", "r")

import heapq

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def is_out_range(x, y):
    return not (0 <= x < n and 0 <= y < n)

def dijkstra(dist, start_x, start_y):
    hq = []
    heapq.heappush(hq, (0, start_x, start_y))
    dist[start_x][start_y] = 0
    while hq:
        d, x, y  = heapq.heappop(hq)
        if dist[x][y] < d:
            continue
        for _x, _y in list(zip(dr, dc)):
            dx, dy = x + _x, y + _y
            if is_out_range(dx, dy): continue
            cost = d + matrix[dx][dy]
            if cost < dist[dx][dy]:
                dist[dx][dy] = cost
                heapq.heappush(hq, (cost, dx, dy))

if __name__ == '__main__':
    t = 0
    INF = sys.maxsize
    while True:
        n = int(input())
        if not n:
            break
        matrix = [list(map(int, input().split())) for _ in range(n)]
        dist = [[INF for _ in range(n)] for _ in range(n)]
        dijkstra(dist, 0, 0)
        t += 1
        print(f'Problem {t}: {dist[n - 1][n - 1] + matrix[0][0]}')