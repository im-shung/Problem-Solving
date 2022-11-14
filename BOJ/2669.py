if __name__ == '__main__':
    n, m = 0, 0
    arr = []
    for i in range(4):
        x1, y1, x2, y2 = map(int, input().split())
        arr.append((x1, y1, x2, y2))
        n = max(x1, x2, n)
        m = max(y1, y2, m)

    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for x1, y1, x2, y2 in arr:
        for i in range(m - y2, m - y1, 1):
            for j in range(x1, x2, 1):
                matrix[i][j] = 1

    # 1로 표시한 부분만 더해주면 그게 넓이
    ans = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if matrix[i][j]:
                ans += 1
    print(ans)