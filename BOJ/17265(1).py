# 114276 KB, 152 ms
from collections import deque

N = int(input())
matrix = [list(input().split()) for _ in range(N)]

mx, mn = -1e9, 1e9

def is_out_range(x, y):
    return not (0 <= x < N and 0 <= y < N)

def is_last_index(x, y):
    return x == N - 1 and y == N -1

def bfs():
    global mx, mn

    Q = deque()
    Q.append((0, 0, matrix[0][0]))

    while Q:
        x, y, sub_result = Q.popleft()
        if is_last_index(x, y):
            if sub_result > mx:
                mx = sub_result
            if sub_result < mn:
                mn = sub_result

        for _x, _y in [(1, 0), (0, 1)]:
            dx, dy = x + _x, y + _y
            if is_out_range(dx, dy):
                continue

            tmp = sub_result
            if matrix[dx][dy].isdigit():
                tmp = eval(str(sub_result) + matrix[x][y] + matrix[dx][dy])
            Q.append((dx, dy, tmp))

bfs()
print(mx, mn)
