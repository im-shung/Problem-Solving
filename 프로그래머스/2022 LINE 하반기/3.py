# 유독 작거나 큰 수가 있으면 체크
# n <= 30 --> 지도가 작다. 
# x <= 1,000,000,000 (10억) --> 시뮬레이션은 불가능

# 1분씩 시간을 흘려보내는 시뮬레이션은 안 되니까 어떻게 풀지 생각해보기 
# 태양과 태양, 태양과 달, 달과 달 모두 독립적으로 계산

# 처음 영향권에 들어가는 시간 t = max(행 차이, 열 차이)
# 시간 m > t 라면 0도 상승
# 시간 m <=t 라면 (m-t+1)도 상승

# 달의 영향권은 (행의 차이 + 열의 차이)로 구할 수 있다. 

n = 3 # 1 ≤ n ≤ 30
m = 2 # 1 ≤ m ≤ 1,000,000,000
fires = [[1, 1]] 
ices = [[3, 3]]
result = [[2, 2, 0], [2 ,1, -1], [0, -1, -1]]

for i in range(n):
    for j in range(n):
        res = 0
        for fire in fires:
            fi, fj = fire[0] - 1, fire[1] - 1
            dist = max(abs(i - fi), abs(j - fj))
            
            delta = 0
            if dist <= m:
                delta += m - dist + 1
            if dist == 0: # 태양 위치
                delta -= 1
            
            res += delta
        
        for ice in ices:
            li, lj = ice[0] - 1, ice[1] - 1
            dist = abs(i - li) + abs(j - lj)
            
            delta = 0
            if dist <= m:
                delta += m - dist + 1
            if dist == 0: # 달 위치
                delta -= 1
            
            res -= delta
        
        print(res, end = ' ')
    print()
            


# def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
#     fire_moves = [(0,0),(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,-1),(1,0),(1,1)]
#     ice_moves = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
#     moves = [(-1,-1),(-1,1),(1,-1),(1,1)]
#     matrix = [[0 for _ in range(n)] for _ in range(n)]
#     Q = deque()
#     for i,j in fires: # 0이면 fire
#         Q.append((0,i-1,j-1))
#     for i,j in ices: # -1 이면 ice
#         Q.append((-1,i-1,j-1))

#     time = 0
#     while time < m:
#         time += 1
#         if time == m+1: break
#         while Q:
#             type,i,j = Q.popleft()
#             if type == 0: 
#                 fire_loc = set()
#                 for _x, _y in fire_moves:
#                     for t in range(1,time+1):
#                         dx, dy = i + _x*t, j + _y*t
#                         if -1 < dx < n and -1 < dy < n:
#                             fire_loc.add((dx,dy))
#                 for x,y in list(fire_loc):
#                     matrix[x][y] += 1
#             else:
#                 ice_loc = set()
#                 minus = set()
#                 for _x, _y in fire_moves:
#                     for t in range(1,time+1):
#                         dx, dy = i + _x*t, j + _y*t
#                         if -1 < dx < n and -1 < dy < n:
#                             ice_loc.add((dx,dy))
#                 for _x, _y in moves:
#                     for t in range(1,time+1):
#                         dx, dy = i + _x*t, j + _y*t
#                         if -1 < dx < n and -1 < dy < n:
#                             minus.add((dx,dy))
#                 for x,y in list(ice_loc-minus):
#                     print(x,y)
#                     matrix[x][y] -= 1
#             print(matrix)        
#         for i,j in fires: # 0이면 fire
#             Q.append((0,i-1,j-1))
#         for i,j in ices: # -1 이면 ice
#             Q.append((-1,i-1,j-1))
    
#     answer = matrix
#     return answer