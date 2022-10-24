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