# SW Expert Academy 
# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYHO7a2JoDFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")      

from collections import deque
import math
INF = math.inf

moves = [(1,0),(0,1),(-1,0),(0,-1)]

def Dijkstra(y,x): 
    D = [[INF] * N for _ in range(N)]
    D[y][x] = 0
    
    queue = deque()
    queue.append((0,0))
    while queue:
        y,x = queue.popleft()
        for _y,_x in moves:
            dy = y+_y
            dx = x+_x
            
            if 0 <= dx < N and 0 <= dy < N:
                cost = 1 # 기본 이동 비용
                if graph[dy][dx] > graph[y][x]: 
                    cost += graph[dy][dx] - graph[y][x] # 높이차만큼 추가해주기 
                if D[dy][dx] > D[y][x] + cost:
                    D[dy][dx] = D[y][x] + cost
                    queue.append((dy,dx))
    return D[N-1][N-1]
for test_case in range(1, int(input()) + 1):
    N = int(input())
    graph =  [list(map(int, input().split())) for _ in range(N)]
    print(f"#{test_case} {Dijkstra(0,0)}")  