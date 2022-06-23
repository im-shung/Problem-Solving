# SW Expert Academy 
# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg

import sys
sys.stdin = open("../sample_input.txt", "r")

from collections import deque

T = int(input())

# 상하좌우 델타값
moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def BFS(y,x):
    distance = [[0] * N for _ in range(N)] 
    
    queue = deque([(y,x)]) # # 큐에 x와 y와 지난 칸 수를 함께 저장 
    while queue:
        y, x = queue.popleft() # 큐가 첫 번째 원소 반환
        if maze[y][x] == 0 or 2:
            maze[y][x] = 1 # 현재위치는 방문했으므로 1로 변경
            
            for _y, _x in moves:
                # 상하좌우 방향으로 인덱스 이동하기
                # 미로 문제는 델타 탐색을 이용!! 
                dy = y + _y   
                dx = x + _x
                
                if (0 <= dx < N) and (0 <= dy < N):
                    if maze[dy][dx] == 0: # 이동할 수 있는 경우
                        distance[dy][dx] = distance[y][x] + 1
                        queue.append((dy,dx))
                    elif maze[dy][dx] == 3: # 도착한 경우
                        return distance[y][x]
                   
    return 0        

for test_case in range(1, T+1):
    N = int(input()) # 미로의 크기

    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        if 2 in maze[i]:
            # [행, 열]
            x = maze[i].index(2)
            y = i
    print(f"#{test_case} {BFS(y,x)}")