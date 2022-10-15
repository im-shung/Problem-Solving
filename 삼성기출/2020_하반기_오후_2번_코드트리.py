from collections import deque

n, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(2**n)]
levels = list(map(int, input().split())) # size는 q
n = 2 ** n
visited =  [[False for _ in range(n)] for _ in range(n)]
result = [[0 for _ in range(n)] for _ in range(n)]
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def printf(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:2}', end = " ")
        print()
    print()


def rotate(x, y, k, move_dir):

    for i in range(x, x + k):
        for j in range(y, y + k):
            _x, _y = moves[move_dir]
            dx, dy = i + _x * k, j + _y * k

            result[dx][dy] = matrix[i][j]

def select(L):
    for i in range(n):
        for j in range(n):
            result[i][j] = 0

    # 레벨이 L일 때 2 L* 2 L 만큼 격자를 선택하여 2 L−1 *2 L−1 만큼 잘라 4등분하여 회전시키게 됩니다. 
    K = (2 ** L)
    k = (2 ** (L-1))
    for i in range(0, n, K):
        for j in range(0, n, K):
            rotate(i, j, k, 0)
            rotate(i, j + k, k, 1)
            rotate(i + k, j + k, k, 2)
            rotate(i + k, j, k, 3)

    for i in range(n):
        for j in range(n):
            matrix[i][j] = result[i][j]

def is_out_range(x, y):
    return not (0 <= x < n and 0 <= y < n)

def melt():
    melt_arr = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                continue
            cnt = 0
            for _x, _y in [(1,0), (0,1), (-1,0), (0,-1)]:
                dx, dy = i + _x, j + _y
                if is_out_range(dx, dy):
                    continue
                if matrix[dx][dy] == 0:
                    continue
                cnt += 1
            if cnt >= 3:
                continue
            melt_arr[i][j] -= 1
    for i in range(n):
        for j in range(n):
            matrix[i][j] += melt_arr[i][j]

def get_size(i, j):
    Q = deque([(i, j)])
    visited[i][j] = True

    size = 1
    while Q:
        i, j = Q.popleft()
        for _x, _y in [(1,0), (0,1), (-1,0), (0,-1)]:
            dx, dy = i + _x, j + _y
            if is_out_range(dx, dy):
                continue
            if matrix[dx][dy] == 0:
                continue
            if visited[dx][dy]:
                continue
            Q.append((dx, dy))
            visited[dx][dy] = True
            size += 1
    return size


def pro():
    global q
    for i in range(q):
        if levels[i] != 0:
            # 1. 회전합니다.
            select(levels[i])
        # 2. 각각의 회전이 끝난 후 빙하에 속한 얼음이 녹습니다.
        melt()
    # 3. 모든 회전을 끝내고 난 뒤에 남아있는 빙하의 총 양과 가장 큰 얼음 군집의 크기를 출력
    mx = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if matrix[i][j] == 0:
                continue
            mx = max(mx, get_size(i, j))
    matrix_sum = sum(matrix, [])
    print(sum(matrix_sum))
    print(mx)

pro()    