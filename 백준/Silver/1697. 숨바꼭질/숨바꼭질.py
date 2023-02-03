from _collections import deque

def bfs(memo, N, K):
    Q = deque()
    Q.append(N)

    while Q:
        x = Q.popleft()
        if x == K:
            return memo[x]
        for dx in (x + 1, x - 1, x * 2):
            if (0 <= dx < 100_001) and memo[dx] == 0:
                memo[dx] = memo[x] + 1
                Q.append(dx)

if __name__ == '__main__':
    N, K = map(int,input().split())
    memo = [0] * 100_001
    print(bfs(memo, N, K))
