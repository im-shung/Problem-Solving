for t in range(1, 11):
    n = int(input())
    matrix = list(map(int, input().split()))
    matrix.sort()

    for _ in range(n):
        matrix[0] += 1
        matrix[-1] -= 1
        matrix.sort()

    print(f"#{t} {matrix[-1] - matrix[0]}")