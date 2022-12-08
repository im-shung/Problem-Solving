# # 113112 KB, 120 ms
N = int(input())
matrix = [list(input().split()) for _ in range(N)]

mx, mn = -1e9, 1e9
def dfs(x, y, res, op):
    global mx, mn

    if x == N - 1 and y == N - 1:
        res = eval(res + op + matrix[x][y])
        print(mx, mn, res)
        if mx < res:
            mx = res
        if res < mn:
            mn = res
        return

    if x == N or y == N:
        return

    for _x, _y in [(1, 0), (0, 1)]:
        if matrix[x][y].isdigit():
            dfs(x + _x, y + _y, str(eval(res + op + matrix[x][y])), op)
        else:
            dfs(x + _x, y + _y, res, matrix[x][y])


dfs(0, 0, '0', '+')
print(mx, mn)