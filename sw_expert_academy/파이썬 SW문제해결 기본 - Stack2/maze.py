# SW Expert Academy 
# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg

import sys
sys.stdin = open("../sample_input.txt", "r")

T = int(input())

# 상하좌우 델타값
moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def dfs(y,x):
    global result
    
    maze[y][x] = 1 # 현재위치는 방문했으므로 1로 변경
    for _y, _x in moves:
        # 상하좌우 방향으로 인덱스 이동하기
        # 미로 문제는 델타 탐색을 이용!! 
        dy = y + _y   
        dx = x + _x
        
        if (0 <= dx < N) and (0 <= dy < N):
            if maze[dy][dx] == 3: # 도착한 경우
                result = 1
                return
            elif maze[dy][dx] == 0: # 이동할 수 있는 경우
                dfs(dy,dx)

for test_case in range(1, T+1):
        N = int(input())
        maze = [list(map(int,input())) for _ in range(N)] # 0은 통로, 1은 벽, 2는 출발, 3은 도착
        x=0; y=0;
        # 시작 지점 구하기 
        for i in range(N):
            if 2 in maze[i]:
                # [행,열]
                x = maze[i].index(2)
                y = i 
                break

        result = 0        
        dfs(y,x)
        print(f"#{test_case} {result}")
