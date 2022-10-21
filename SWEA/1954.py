dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_out_range(x, y):
    return not (0 <= x < n and 0 <= y < n)

for t in range(1, int(input()) + 1):
    n = int(input())
    s = [[0 for _ in range(n)] for _ in range(n)]

    r, c, dist = 0, 0, 0
    for num in range(1, n * n + 1):
        s[r][c] = num
        r += dr[dist]
        c += dc[dist]

        if is_out_range(r, c) or s[r][c] != 0:
            r -= dr[dist]
            c -= dc[dist]
            dist = (dist + 1) % 4
            r += dr[dist]
            c += dc[dist]
    print(f'#{t} ')
    for ss in s:
        print(*ss)