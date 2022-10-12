from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

arr = [[5],[6,3,1,4],[2]] # rotated_right 상태

def rotated_down():
    tmp = [ arr[2][0], arr[1][1], arr[0][0], arr[1][3] ]
    arr[1][1] = tmp[0]
    arr[0][0] = tmp[1]
    arr[1][3] = tmp[2]
    arr[2][0] = tmp[3]

def rotated_top():
    tmp = [ arr[2][0], arr[1][1], arr[0][0], arr[1][3] ]
    arr[1][3] = tmp[0]
    arr[2][0] = tmp[1]  
    arr[1][1] = tmp[2]
    arr[0][0] = tmp[3]
      
def rotated_left():
    tmp = arr[1][3]
    arr[1][1:4] = arr[1][:3]
    arr[1][0] = tmp

def rotated_right():
    tmp = arr[1][0]
    arr[1][0:3] = arr[1][1:4]
    arr[1][3] = tmp    

def is_out_range(x, y):
    return not (0 <= x < n and 0 <= y < n)

def get_score(x, y):
    Q = deque()
    Q.append((x, y))
    visited = [(x, y)]
    cnt = 1

    while Q:
        i, j = Q.popleft()
        val = matrix[i][j]
        for _x, _y in [(0,1), (1,0), (-1,0), (0,-1)]:
            dx, dy = i + _x, j + _y
            if is_out_range(dx, dy):
                continue
            if (dx, dy) in visited:
                continue
            if val != matrix[dx][dy]:
                continue 
            Q.append((dx, dy))
            visited.append((dx, dy))
            cnt += 1
    # print(x, y, cnt)
    return matrix[x][y] * cnt

def is_boundary_top(x, y):
    return (x == 0)

def is_boundary_down(x, y):
    return (x == n - 1)

def is_boundary_left(x, y):
    return (y == 0)

def is_boundary_right(x, y):
    return (y == n - 1)

def pro():
    global m

    score = 0
    direction = "right"
    i, j = (0, 1)
    while m > 0:
        score += get_score(i, j)

        if arr[1][1] > matrix[i][j]: # 90도 시계방향 회전
            if direction == "right":
                direction = "down"
            elif direction == "left":
                direction = "top"
            elif direction == "top":
                direction = "right"
            elif direction == "down":
                direction = "left"
        elif arr[1][1] < matrix[i][j]:
            if direction == "right":
                direction = "top"
            elif direction == "left":
                direction = "down"
            elif direction == "top":
                direction = "left"
            elif direction == "down":
                direction = "right"
        # print(arr[1][1], matrix[i][j])
        if direction == "top":
            if is_boundary_top(i, j):
                direction = "down"
                rotated_down()
                i += 1
            else:
                rotated_top()
                i -= 1
        elif direction == "down":
            if is_boundary_down(i, j):
                direction = "top"
                rotated_top()
                i -= 1
            else:
                rotated_down()
                i += 1
        elif direction == "right":
            if is_boundary_right(i, j):
                direction = "left"
                rotated_left()
                j -= 1
            else:
                rotated_right()
                j += 1
        elif direction == "left":
            if is_boundary_left(i, j):
                direction = "right"
                rotated_right()
                j += 1
            else:
                rotated_left()
                j -= 1
        # print(direction)
        m -= 1    
    print(score)
pro()