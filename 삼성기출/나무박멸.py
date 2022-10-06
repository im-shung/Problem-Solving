from collections import deque

n, m, k, c = map(int,input().split())
# matrix = [list(map(int,input().split())) for _ in range(n)]
matrix = [[[0,0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    s = list(map(int,input().split()))
    for j in range(n):
        matrix[i][j] = [s[j],0] # (i: 나무 수, j: 제초제가 남아있는 년수)


dead_tree = 0
year = 0
while year < m:        
    if year > 0:
        for i in range(n):
            for j in range(n):
                if matrix[i][j][0] == -2:
                    rest_year = matrix[i][j][1]
                    if rest_year - 1 == -1:           
                        matrix[i][j] = [0, 0]
                    else:
                        matrix[i][j][1] -= 1
    # 성장
    for i in range(n):
        for j in range(n):
            if matrix[i][j][0] > 0: 
                cnt = 0
                for _x, _y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    dx, dy = i + _x, j + _y
                    if 0 <= dx < n and 0 <= dy < n:
                        if matrix[dx][dy][0] > 0: # matrix[dx][dy]가 나무 칸이면 cnt + 1
                            cnt += 1
                matrix[i][j][0] += cnt # 인접한 4칸에 있는 나무의 수 만큼 더해진다.

    # 번식
    Q = deque()
    for i in range(n):
        for j in range(n):
            if matrix[i][j][0] > 0: 
                Q.append((i,j,matrix[i][j][0]))

    memo = []
    tree_set = set()
    while Q:
        i, j, matrix_val = Q.popleft()
        tree_set.add((i,j))
        cnt = 0
        _memo = []
        for _x, _y in [(1,0),(-1,0),(0,1),(0,-1)]:
            dx, dy = i + _x, j + _y
            if 0 <= dx < n and 0 <= dy < n:
                if matrix[dx][dy][0] == 0: # matrix[dx][dy]가 빈 칸이면 cnt + 1
                    cnt += 1
                    _memo.append((dx,dy))

        # 인접한 4칸에 각 칸의 나무 그루 수에서 총 번식이 가능한 칸의 개수만큼 나누어진 그루 수만큼 번식
        if cnt > 0:
            val = matrix_val // cnt
            for x, y in _memo:
                tree_set.add((x,y))
                memo.append((x,y,val))
                
    for x, y, val in memo:
        matrix[x][y][0] += val # 모든 나무 칸에서 번식이 이루어지기에 += 를 쓴다.

    # 제초제 위치 선정
    # 나무가 가장 많이 박멸되는 칸
    tree_set = list(tree_set)
    tree_set.sort()
    mx = 0        
    answer = (0, 0)       
    for i, j in tree_set:
        _mx = matrix[i][j][0]
        for _x, _y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            for _k in range(1, k + 1):
                dx, dy = i + _x * _k, j + _y * _k
                if 0 <= dx < n and 0 <= dy < n:
                    if matrix[dx][dy][0] in [0, -1]:
                        break
                    else:
                        _mx += matrix[dx][dy][0]
        if mx < _mx:
            mx = _mx
            answer = (i, j)


    # 제초제 뿌리기 (c년동안 진행)
    i, j = answer
    for _x, _y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        for _k in range(k + 1):
            dx, dy = i + _x * _k, j + _y * _k
            if 0 <= dx < n and 0 <= dy < n:
                if matrix[dx][dy][0] in [0, -1]:
                    if matrix[dx][dy][0] == 0:
                        matrix[dx][dy] = [-2, c]
                    break
                else:
                    if matrix[dx][dy][0] != -2:
                        dead_tree += matrix[dx][dy][0]
                    matrix[dx][dy] = [-2, c]

    year += 1

print(dead_tree)