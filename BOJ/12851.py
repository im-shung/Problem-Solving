from _collections import deque

def bfs(dist, N, K):
    queue = deque()
    queue.append(N)

    dist[N][0] = 0 # 가장 빠른 시간
    dist[N][1] = 1 # 가장 빠른 시간으로 찾는 방법 수

    while queue:
        x = queue.popleft()
        if x == K:
            continue
        for dx in (x + 1, x - 1, x * 2):
            if 0 <= dx < 100_001:
                if dist[dx][0] == -1:
                    dist[dx][0] = dist[x][0] + 1
                    dist[dx][1] = dist[x][1]
                    queue.append(dx)
                elif dist[dx][0] == dist[x][0] + 1:
                    dist[dx][1] += dist[x][1]

if __name__ == '__main__':
    N, K = map(int,input().split())
    dist = [[-1, 0] for _ in range(100_001)]
    bfs(dist, N, K)
    print(dist[K][0])
    print(dist[K][1])
