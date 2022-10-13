n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
moving = [tuple(map(int,input().split())) for _ in range(m)]
# bomb = [[0 for _ in range(n)] for _ in range(n)]
# bomb[n - 1][0] = 1
# bomb[n - 1][1] = 1
# bomb[n - 2][0] = 1
# bomb[n - 2][1] = 1

location = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
direction = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
add = [[0 for _ in range(n)] for _ in range(n)]


def move_in(x, y):
    if x < 0: x += n
    elif x >= n: x -= n

    if y < 0: y += n
    elif y >= n: y -=n

    return (x, y)

def move(rule):
    global direction, location

    d, p = rule # 이동 방향 d, 이동 칸 수 p
    for i in range(len(location)):
        x, y = location[i]
        dx, dy = x + direction[d - 1][0] * p, y + direction[d - 1][1] * p
        location[i] = move_in(dx, dy)
def is_out_range(x, y):
    return not (0 <= x < n and 0 <= y < n)        

def insert():
    global matrix

    for x, y in location:
        matrix[x][y] += 1
    
def grow():
    global matrix, add, location

    for i in range(n):
        for j in range(n): 
            add[i][j] = 0

    for x, y in location:
        for _x, _y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            dx, dy = x + _x, y + _y
            if is_out_range(dx, dy):
                continue
            if matrix[dx][dy] < 1:
                continue
            add[x][y] += 1

    for i in range(n):
        for j in range(n): 
            matrix[i][j] += add[i][j]  

def cut():
    global matrix, location
    
    # 특수 영양제 위치 초기화
    new_location = []

    for i in range(n):
        for j in range(n): 
            if matrix[i][j] < 2:
                continue
            if (i, j) in location:
                continue
            matrix[i][j] -= 2
            new_location.append((i, j))
    location = new_location      

def printf(arr):
    for i in range(n):
        print(*arr[i])

def pro():
    global m

    year = 0
    while year < m:

        # 1. 특수 영양제를 이동 규칙에 따라 이동시킵니다.
        move(moving[year])

        # 2. 특수 영양제를 이동 시킨 후 해당 땅에 특수 영양제를 투입합니다.
        insert()

        # 3. 특수 영양제를 투입한 리브로수의 대각선으로 인접한 방향에 높이가 1 이상인 리브로수가 있는 만큼 높이가 더 성장합니다. 대각선으로 인접한 방향이 격자를 벗어나는 경우에는 세지 않습니다.
        grow()
        
        # 4. 특수 영양제를 투입한 리브로수를 제외하고 높이가 2 이상인 리브로수는 높이 2를 베어서 잘라낸 리브로수로 특수 영양제를 사고, 해당 위치에 특수 영양제를 올려둡니다.
        cut()
        
        year += 1

    matrix_sum = sum(matrix, [])
    print(sum(matrix_sum))    
pro()