def dfs(x):
    global result

    if x == n:
        result += 1
        return

    for y in range(n):
        if y in columns \
                or (x + y) in l_diagonals \
                or (x - y) in r_diagonals:
            continue

        columns.add(y)
        l_diagonals.add(x + y)
        r_diagonals.add(x - y)

        dfs(x + 1)

        columns.remove(y)
        l_diagonals.remove(x + y)
        r_diagonals.remove(x - y)


for t in range(1, int(input()) + 1):
    n = int(input())
    result = 0
    columns, l_diagonals, r_diagonals = set(), set(), set()
    dfs(0)
    print(f'#{t} {result}')