from collections import deque

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

def is_out_range(x, y):
    return not (0 <= x < n and 0 <= y < n)

def find_group():
    global group, group_cnt, group_size

    def bfs(i, j, num):
        group_size[num] += 1
        group[i][j] = num

        Q = deque()
        Q.append((i,j))
        
        while Q:
            i, j = Q.popleft()
            for _x, _y in [(1,0), (0,1), (-1,0), (0,-1)]:
                dx, dy = i + _x, j + _y
                if is_out_range(dx, dy): continue
                if group[dx][dy] != 0: continue
                if matrix[i][j] != matrix[dx][dy]: continue
                group[dx][dy] = num
                group_size[num] += 1
                Q.append((dx, dy))

    group = [[0 for _ in range(n)] for _ in range(n)]
    group_size = [0] * (n * n + 1)
    group_cnt = 0
        
    for i in range(n):
        for j in range(n):
            if group[i][j] != 0: continue
            group_cnt += 1
            bfs(i, j, group_cnt)


def get_score():
    global group, group_cnt, group_size

    ret = 0
    for i in range(n):
        for j in range(n):
            for _x, _y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                dx, dy = i + _x, j + _y
                if is_out_range(dx, dy): continue
                if group[i][j] == group[dx][dy]: continue
                A = group[i][j]
                B = group[dx][dy]
                ret += (group_size[A] + group_size[B]) * matrix[i][j] * matrix[dx][dy]

    return ret;           


def rotate_etc(i, j, ni, nj, m):
    global matrix

    arr = [[] for _ in range(m)]
    arr[0] = matrix[i][j: nj + 1]
    for x in range(i + 1, ni + 1):
        arr[x - i] = matrix[x][j: nj + 1]
    
    # print(arr)
    arr = list(map(list, zip(*arr[::-1])))

    k = 0
    for x in range(i, ni + 1):
        matrix[x][j: nj + 1] = arr[k]
        k += 1


def rotate():
    global matrix

    m = n//2 

    # 가운데 십자가 부분 반시계방향 90도 돌리기
    arr = list(map(list, zip(*matrix)))[::-1]
    tmp_r, tmp_c = [], []
    for i in range(n): tmp_r.append(arr[i][m])
    for _ in range(n): tmp_c = (arr[m])
    matrix[m] = tmp_c
    for i in range(n): matrix[i][m] = tmp_r[i]

    # 이외 부분 시계방향 90도 돌리기
    rotate_etc(0, 0, m - 1, m - 1, m)
    rotate_etc(0, m + 1, m - 1, n - 1, m)
    rotate_etc(m + 1, 0, n - 1, m - 1, m)
    rotate_etc(m + 1, m + 1, n - 1, n - 1, m)

def pro():
    ans = 0
    for _ in range(4):
        # 1. 그룹 찾기
        find_group()

        # 2. 예술점수 구하기
        ans += get_score()//2

        # 3. 회전
        rotate()

    print(ans)

pro()