from collections import Counter

N = 9

def check():
    # 가로
    for i in range(N):
        result = Counter(puzzle[i]).most_common(1)  # [(8, 1)]
        if result[0][1] > 1:
            return 0
    # 세로
    for i in range(N):
        arr = []
        for j in range(N):
            arr.append(puzzle[j][i])
        result = Counter(arr).most_common(1)
        if result[0][1] > 1:
            return 0

    # 3x3 격자
    for i in range(0, N - 2, 3):
        for j in range(0, N - 2, 3):
            arr = []
            for a in range(3):
                for b in range(3):
                    arr.append(puzzle[i + a][j + b])
            result = Counter(arr).most_common(1)
            if result[0][1] > 1:
                return 0

    return 1

for t in range(1, int(input()) + 1):
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    answer = check()
    print(f'#{t} {answer}')
