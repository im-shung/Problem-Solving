for t in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int,input())) for _ in range(n)]
    result = 0
    m = n // 2
    for i in range(n):
        for j in range(n):
            if (abs(m- i) + abs(m - j)) <= m: # (행 차이 + 열 차이)
                result += matrix[i][j]
    print(f'#{t} {result}')