import sys
sys.stdin = open("C:\Program_study\AlgorithmStudy\sample_input.txt", "r")

def is_out_range(x, y):
    return not (0 <= x <= N and 0 <= y <= M)

if __name__ == '__main__':
    N, M, L, K = map(int, input().split())
    star = []
    for _ in range(K):
        x, y = map(int, input().split())
        star.append((x, y))

    visited = [[False for _ in range(M + 1)] for _ in range(N + 1)]
    mx = 0
    for k in range(K):
        X, Y = star[k]
        for x in range(X -K - 1, X + 1, 1):
            for y in range(Y - K - 1, Y + 1, 1):
                dx, dy = x + L, y + L
                if is_out_range(dx, dy) or is_out_range(x, y): continue
                if visited[x][y]: continue
                count = 0
                for nk in range(K):
                    nx, ny = star[nk]
                    if x <= nx <= dx and y <= ny <= dy:
                        count += 1
                visited[x][y] = True
                mx = max(count, mx)
    print(K - mx)
