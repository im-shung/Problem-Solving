for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [[0 for _ in range(i)] for i in range(1, n + 1)]
    arr[0][0] = 1
    for i in range(1, n):
        for j in range(i + 1):
            if j >= 1:
                arr[i][j] += arr[i - 1][j - 1]
            if j <= i - 1:
                arr[i][j] += arr[i - 1][j]
    print(f'#{t}')
    for p in arr:
        print(*p)