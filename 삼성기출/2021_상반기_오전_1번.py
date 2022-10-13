from collections import defaultdict

def is_out_range(x, y):
    return not (0 <= x < n and 0 <= y < n)

# 4방향으로 인접한 칸 중 앉아있는 좋아하는 친구의 수 구하기
def get_like(num, i, j):
    global std, matrix

    like, blank = 0, 0
    for _x, _y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        dx, dy = i + _x, j + _y
        if is_out_range(dx, dy):
            continue
        if matrix[dx][dy] == 0:
            blank += 1
            continue
        if not matrix[dx][dy] in std[num]:
            continue
        like += 1
    return (like, blank)

# 학생 탑승
def move(num):
    global std, matrix

    location = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0: # 항상 비어있는 칸으로만 이동합니다.
                continue
            like, blank = get_like(num, i, j)    
            location.append([like, blank, i, j])

    # 1. 격자를 벗어나지 않는 4방향으로 인접한 칸 중 앉아있는 좋아하는 친구의 수가 가장 많은 위치로 갑니다.
    # 2. 만약 1번 조건을 만족하는 칸의 위치가 여러 곳이라면, 그 중 인접한 칸 중 비어있는 칸의 수가 가장 많은 위치로 갑니다. 단 이때 격자를 벗어나는 칸은 비어있는 칸으로 간주하지 않습니다.
    # 3. 만약 2번 조건까지 동일한 위치가 여러 곳이라면, 그 중 행 번호가 가장 작은 위치로 갑니다.
    # 4. 만약 3번 조건까지 동일한 위치가 여러 곳이라면, 그 중 열 번호가 가장 작은 위치로 갑니다.
    # 1, 2, 3, 4를 모두 고려한 sort
    location.sort(key = lambda x: ( -x[0], -x[1], x[2], x[3] ))
    x, y = location[0][2], location[0][3]
    matrix[x][y] = num
    
def get_score():
    global std, matrix, likes
    
    score = 0
    for i in range(n):
        for j in range(n):
            num = matrix[i][j]
            like, blank = get_like(num, i, j)
            score += likes[like]
    return score

def printf(arr):
    for i in range(n):
        print(*arr[i])
    print()

## pro()
n = int(input())
std = defaultdict(list)
matrix = [[0 for _ in range(n)] for _ in range(n)]
likes = [0, 1, 10, 100, 1000]

for _ in range(n * n):
    s = list(map(int,input().split()))
    std[s[0]] = s[1:]
    move(s[0])

print(get_score())