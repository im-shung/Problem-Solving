# 시계방향으로 90도 회전
def rotate(arr):
    m = len(arr)
    temp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(m):
        for j in range(m):
            temp[j][m - 1 - i] = arr[i][j]

    return temp

def printArr(arr):
    return ''.join(map(str,arr))

for t in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    matrix_90 = rotate(matrix)
    matrix_180 = rotate(matrix_90)
    matrix_270 = rotate(matrix_180)

    print(f'#{t}')
    for i in range(n):
        print(printArr(matrix_90[i]), printArr(matrix_180[i]),printArr(matrix_270[i]))