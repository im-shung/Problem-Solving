# 완전탐색
for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for x in range(n - m + 1):
        for y in range(n - m + 1):
            tmp = 0
            for i in range(x, x + m):
                tmp += sum(arr[i][y: y + m])
            result = max(result,tmp)


    print(f'#{t} {result}')

# 누적합
for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [[0 for _ in range(n + 1)]]
    for _ in range(n):
        arr.append([0] + list(map(int, input().split())))
    result = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            arr[i][j] = arr[i-1][j] + arr[i][j]

    for i in range(1, n - m + 2):
        for j in range(1, n - m + 2):
            result = max(result, sum(arr[i + m - 1][j: j + m]) - sum(arr[i - 1][j: j + m]))

    print(f'#{t} {result}')