R, C, Q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
n_arr = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
for i in range(1, R + 1):
    for j in range(1, C + 1):
        n_arr[i][j] = n_arr[i - 1][j] + n_arr[i][j - 1] + arr[i - 1][j - 1] - n_arr[i - 1][j - 1]

for _ in range(Q):
    r1, c1, r2, c2 = map(int,input().split())
    cnt = (r2 - r1 + 1) * (c2 - c1 + 1)
    ans = (n_arr[r2][c2] - n_arr[r2][c1 - 1] - n_arr[r1 - 1][c2] + n_arr[r1 - 1][c1 - 1]) // cnt
    print(ans)