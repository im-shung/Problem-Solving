from collections import deque

n, m, k, c = map(int,input().split())
matrix = [[[0,0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    s = list(map(int,input().split()))
    for j in range(n):
        matrix[i][j] = [s[j], 0] # (i: 나무 수, j: 제초제가 남아있는 년수)

def is_out_range(x, y):
    return not (0 <= x < n and 0 <= y < n)

def grow():
    global matrix
    
    for i in range(n):
        for j in range(n):
            # 나무 칸이면 성장한다.
            if matrix[i][j][0] > 0: 
                cnt = 0
                for _x, _y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    dx, dy = i + _x, j + _y
                    if is_out_range(dx,dy): continue
                    if matrix[dx][dy][0] > 0: # matrix[dx][dy]가 나무 칸이면 cnt + 1
                        cnt += 1
                matrix[i][j][0] += cnt # 인접한 4칸에 있는 나무의 수 만큼 더해진다.

# 기존에 있었던 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행합니다.
def breed():
    global matrix
    
    # Q에 기존 나무 칸 위치(i, j)와 그루 수 삽입 
    Q = deque()
    for i in range(n):
        for j in range(n):
            if matrix[i][j][0] > 0: 
                Q.append( (i ,j, matrix[i][j][0]) )

    memo = []
    while Q:
        i, j, tree_num = Q.popleft()
        cnt = 0
        _memo = []
        for _x, _y in [(1,0), (-1,0), (0,1), (0,-1)]:
            dx, dy = i + _x, j + _y
            if is_out_range(dx,dy): continue
            if matrix[dx][dy][0] == 0: # 벽(-1), 다른 나무(양수), 제초제(-2) 모두 없는 칸
                cnt += 1
                _memo.append( (dx, dy) )

        # 각 칸의 나무 그루 수(tree_num)에서 총 번식이 가능한 칸의 개수(cnt)만큼 나누어진 그루 수만큼 번식이 되며, 나눌 때 생기는 나머지는 버립니다. 
        if cnt > 0:
            val = tree_num // cnt
            for x, y in _memo:
                memo.append( (x, y, val) )
                
    # 번식의 과정은 모든 나무에서 동시에 일어나게 됩니다.            
    for x, y, val in memo:
        matrix[x][y][0] += val 

# 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다. 
# 제초제를 뿌릴 때 4개의 대각선 방향으로 k칸만큼 전파되게 됩니다. 
# 단 전파되는 도중 벽이 있거나 나무가 아예 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다. 
# 만약 박멸시키는 나무의 수가 동일한 칸이 있는 경우에는 행이 작은 순서대로, 만약 행이 같은 경우에는 열이 작은 칸에 제초제를 뿌리게 됩니다.
def select():
    global matrix, trees
    
    trees = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j][0] > 0: 
                trees.append([i, j])
    
    trees = list(trees)
    sorted(trees, key = lambda x: (x[0], x[1]))
    
    mx = 0 
    location = (0, 0)
    for i, j in trees:
        _mx = matrix[i][j][0]
            
        for _x, _y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            
            for _k in range(1, k + 1):
                dx, dy = i + _x * _k, j + _y * _k
                if is_out_range(dx, dy): 
                    break
                if matrix[dx][dy][0] <= 0:
                    break
                _mx += matrix[dx][dy][0]
                    
        if mx < _mx:
            mx = _mx
            location = (i, j)
            
    return location
   
# 제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라지게 됩니다. 
# 제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지됩니다.
def execute(location):
    global matrix
    
    i, j = location
    tree = 0
    if matrix[i][j][0] > 0:
        
        tree += matrix[i][j][0]
        matrix[i][j] = [-2, c]
        
        for _x, _y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            
            for _k in range(1, k + 1):
                dx, dy = i + _x * _k, j + _y * _k
                if is_out_range(dx, dy): 
                    break
                if matrix[dx][dy][0] == -1:
                    break
                if matrix[dx][dy][0] <= 0:
                    matrix[dx][dy] = [-2, c]
                    break
                tree += matrix[dx][dy][0]
                matrix[dx][dy] = [-2, c]
                
    return tree

def year_check():
    global matrix
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j][0] == -2:
                rest_year = matrix[i][j][1]
                if rest_year == 0:
                    matrix[i][j] = [0, 0]
                else:
                    matrix[i][j][1] -= 1
    
def pro():
    year = 0
    dead_tree = 0
    while year < m:
        # 1. 나무의 성장
        grow()
        # 2. 나무의 번식
        breed()
        # 3. 제초제를 뿌릴 위치 선정
        location = select()
        # 4. 제초제를 뿌리는 작업 진행
        dead_tree += execute(location)
        # 5. 제초제 년도 체크
        year_check()
        
        year += 1
        
        
    print(dead_tree)
pro()