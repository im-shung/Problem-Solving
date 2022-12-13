M, N = map(int, input().split())
matrix = [[1 for _ in range(M)] for _ in range(M)] # 애벌레 크기에 대한 격자
grow_matrix = [[0 for _ in range(M)] for _ in range(M)] # 애벌레가 자라는 정도에 대한 격자

mov = [(0, -1), (-1, -1), (-1, 0)] # 왼쪽(L), 왼쪽 위(D), 위쪽(U)

def is_out_range(x, y):
    return not (0 <= x < M and 0 <= y < M)

def print_matrix():
    for _ in range(M):
        print(*matrix[_])
    print()

for _ in range(N):
    grow = list(map(int, input().split()))
    idx = 0

    for i in range(M - 1, -1, -1): # 제일 왼쪽 열
        while grow[idx] == 0:
            idx += 1
        matrix[i][0] += idx
        grow_matrix[i][0] = idx
        grow[idx] -= 1

    for i in range(1, M, 1): # 제일 위쪽 행, (0,0)은 제일 왼쪽 열에서 체크됨
        while grow[idx] == 0:
            idx += 1
        matrix[0][i] += idx
        grow_matrix[0][i] = idx
        grow[idx] -= 1

    for i in range(1, M):
        for j in range(1, M):
            mx = -1
            for _i, _j in mov:
                di, dj = i + _i, j + _j
                if is_out_range(di, dj):
                    continue
                mx = max(mx, grow_matrix[di][dj])
            grow_matrix[i][j] += mx
            matrix[i][j] += mx

    grow_matrix = [[0 for _ in range(M)] for _ in range(M)]

print_matrix()