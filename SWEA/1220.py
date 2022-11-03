for t in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # N극(1)이 윗부분, S극(2)이 아래부분

    result = 0
    for col in range(n):
        stack = []
        for row in range(n):
            if matrix[row][col] == 0: continue
            if matrix[row][col] == 1:
                stack.append(1)
            elif matrix[row][col] == 2:
                if stack:
                    result += 1
                    stack = []

    print(f'#{t} {result}')


