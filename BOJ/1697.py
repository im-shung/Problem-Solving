from _collections import deque

def bfs(dist, N, K):
    Q = deque()
    Q.append(N)

    while Q:
        x = Q.popleft()
        if x == K:
            return dist[x]
        for dx in (x + 1, x - 1, x * 2):
            if (0 <= dx < 100_001) and dist[dx] == -1:
                dist[dx] = dist[x] + 1
                Q.append(dx)

if __name__ == '__main__':
    N, K = map(int,input().split())
    dist = [-1] * 100_001
    print(bfs(dist, N, K))