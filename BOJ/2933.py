import sys
sys.stdin = open("../sample_input.txt", "r")

from _collections import deque

def printf(arr):
    for a in range(1, R + 1):
        for b in range(C):
            if arr[a][b] != ".":
                print("x", end = "")
            else:
                print(arr[a][b], end = "")
        print()

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def is_out_range(x, y):
    return not (0 <= x <= R and 0 <= y < C)

def bfs(matrix, x, y, group_count):
    queue = deque()
    queue.append((x,y))
    visited = [[False for _ in range(C)] for _ in range(R + 1)]
    visited[x][y] = True
    matrix[x][y] = group_count
    while queue:
        x, y = queue.popleft()
        for _x, _y in list(zip(dr, dc)):
            dx, dy = x + _x, y + _y
            if is_out_range(dx, dy) or visited[dx][dy] or matrix[dx][dy] == ".": continue
            if matrix[dx][dy] == "x":
                matrix[dx][dy] = group_count
                queue.append((dx, dy))


def cluster_seperate(matrix, x, y, group_count):
    # x,y : 미네랄 파괴된 좌표
    # 같은 클러스터인 인접한 좌표
    # 분리되었다면 로직을 어떻게 짜야하는가?
    # 1) 전체 bfs를 돌려 클러스터 초기화 -> 공중에 떠있는 클러스터 찾아서 떨어트리기
    # 2) 미네랄 파괴된 인접 4부분만 bfs돌려 바닥에 있지 않으면 떨어트리기?

    temp = matrix[x][y]

    visited = [[False for _ in range(C)] for _ in range(R + 1)]
    # bfs: "x"로 초기화
    queue = deque()
    queue.append((x, y))
    visited = [[False for _ in range(C)] for _ in range(R + 1)]
    visited[x][y] = True
    matrix[x][y] = "."
    while queue:
        x, y = queue.popleft()
        for _x, _y in list(zip(dr, dc)):
            dx, dy = x + _x, y + _y
            if is_out_range(dx, dy) or visited[dx][dy] or matrix[dx][dy] == ".": continue
            if matrix[dx][dy] == temp:
                matrix[dx][dy] = "x"
                queue.append((dx, dy))

    for c in range(C):
        if matrix[R][c] == "x":
            bfs(matrix, R, c, group_count)
            group_count += 1


if __name__ == '__main__':
    R, C = map(int, input().split())
    matrix = [["." for _ in range(C)] for _ in range(R + 1)]
    for r in range(1, R + 1):
        matrix[r] = list(input())
    n = int(input())
    s = list(map(int, input().split()))
    # 문제에서 높이 1은 행렬의 가장 바닥, R은 가장 위를 의미한다. 라고 했으니 반대로 바꾸기
    for i in range(n):
        s[i] = R - s[i] + 1

    group = []
    group_count = 0
    # 1. 클러스터 초기화
    for x in range(1, R + 1):
        for y in range(C):
            if matrix[x][y] == "x":
                group.append(True)
                bfs(matrix, x, y, group_count)
                group_count += 1

    # 2. 막대 던지기
    flag = True
    boom = False
    for r in s:
        if flag:
            flag = False
            for c in range(C):
                if not matrix[r][c] == ".":
                    boom = True
                    break
        else:
            flag = True
            for c in range(C - 1, -1, -1):
                if not matrix[r][c] == ".":
                    boom = True
                    break

        if not boom: continue # 미네랄이 파괴가 안됐다면 다시 막대 던지기

        # 3. 미네랄 파괴 (boom = True)
        # 3-1. 클러스터가 분리되었는지 확인
        # 3-2. 클러스터가 분리되었다면 새로 클러스터 배정
        cluster_seperate(matrix, r, c, group_count)

        # 3-3. 공중에 떠 있는 클러스터가 있는 지 확인
        c_arr = []
        height = 0
        for x in range(R, 0, -1):
            for y in range(C):
                if matrix[x][y] == "x":
                    height = R - x
                    c_arr.append((x, y))
            if c_arr:
                break

        # 3-4. 떨어트리고 다른 클러스터 위에 떨어지면 합친다.
        fall = 0
        for x, y in c_arr:
            for dx in range(x + 1, R + 1):
                if matrix[dx][y] != ".":
                    fall = dx
                    break

        for x in range(R, 0, -1):
            for y in range(C):
                if matrix[x][y] == "x":
                    matrix[x][y] = "."
                    matrix[x + height][y] = "x"
                    if fall != 0:
                        matrix[fall - 1][y] = matrix[fall][y]

        for c in range(C):
            if matrix[R][c] == "x":
                bfs(matrix, R, c, group_count)
                group_count += 1

    printf(matrix)


