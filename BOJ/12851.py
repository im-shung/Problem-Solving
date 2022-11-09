from _collections import deque

def bfs(memo, N, K):
    queue = deque()
    queue.append(N)

    memo[N][0] = 0 # 가장 빠른 시간
    memo[N][1] = 1 # 가장 빠른 시간으로 찾는 방법 수

    while queue:
        x = queue.popleft()
        if x == K:
            continue
        for dx in (x + 1, x - 1, x * 2):
            if 0 <= dx < 100_001:
                if memo[dx][0] == 0:
                    memo[dx][0] = memo[x][0] + 1
                    memo[dx][1] = memo[x][1]
                    queue.append(dx)
                elif memo[dx][0] == memo[x][0] + 1:
                    memo[dx][1] += memo[x][1]

if __name__ == '__main__':
    N, K = map(int,input().split())
    memo = [[0, 0] for _ in range(100_001)]
    bfs(memo, N, K)
    print(memo[K][0])
    print(memo[K][1])
