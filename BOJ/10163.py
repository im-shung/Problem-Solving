from collections import defaultdict

NUM = 1_000
SIZE = NUM + 1

if __name__ == '__main__':
    N = int(input())

    matrix = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    count = defaultdict(int)

    for n in range(1, N + 1):
        x, y, w, h = map(int, input().split())
        for i in range(y, y + h): # 행
            for j in range(x, x + w): # 열
                matrix[NUM - i][j] = n
        count[n] = 0

    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j]:
                count[matrix[i][j]] += 1

    for n in range(1, N + 1):
        print(count[n])
