K = 8

for t in range(1, 11):
    n = int(input())
    matrix = [list(input()) for _ in range(K)]

    result = 0
    for i in range(K):
        for j in range(K - n + 1):

            # 가로
            if matrix[i][j:j+n] == matrix[i][j:j+n][::-1]:
                result += 1

            # 세로
            arr = []
            for v in range(n):
                arr.append(matrix[j + v][i])
            if arr == arr[::-1]:
                result += 1

    print(f'#{t} {result}')