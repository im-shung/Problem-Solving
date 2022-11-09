import sys
sys.stdin = open("../sample_input.txt", "r")

from collections import deque

INF = 1e9

def bfs(X):
    Q = deque()
    memo = [INF for _ in range(100_001)]
    visited = [False for _ in range(100_001)]

    Q.append(X)
    memo[X] = 0
    visited[X] = True

    while Q:
        x = Q.popleft()
        if x == K: return memo[x]
        for dx in [x + 1, x - 1, x * 2]:
            if dx < 0 or dx > 100_000 or visited[dx]: continue
            if memo[x] + 1 < memo[K]:
                Q.append(dx)
                memo[dx] = memo[x] + 1
                visited[dx] = True

if __name__ == '__main__':
    N, K = map(int,input().split())
    print(bfs(N))
