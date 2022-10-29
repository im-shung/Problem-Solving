n = 100

for _ in range(1, 11):
    t = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    sum_arr = []
    c = 0
    d = 0
    for i in range(n):
        a = 0
        b = 0
        for j in range(n):
            a += matrix[i][j]
            b += matrix[j][i]
            if i == j:
                c += matrix[i][j]
            if i + j == n - 1:
                d += matrix[i][j]
        sum_arr.append(a)
        sum_arr.append(b)
    sum_arr.append(c)
    sum_arr.append(d)
    print(f'#{t} {max(sum_arr)}')