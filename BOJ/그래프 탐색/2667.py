from _collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def is_out_range(x, y):
    return not (0 <= x < n and 0 <= y < n)

def bfs(x, y, group_size, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1
        matrix[x][y] = group_size
        for _x, _y in list(zip(dr, dc)):
            dx, dy = x + _x, y + _y
            if is_out_range(dx, dy) or visited[dx][dy] or matrix[dx][dy] == 0: continue
            if matrix[dx][dy] == '1':
                matrix[dx][dy] = group_size
                queue.append((dx, dy))
    return count

if __name__ == '__main__':
    n = int(input())
    matrix = [list(input()) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    group_size = 0
    group_count = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '1':
                group_size += 1
                group_count.append(bfs(i, j, group_size, visited))

    print(len(group_count))
    group_count.sort()
    for gc in group_count:
        print(gc)