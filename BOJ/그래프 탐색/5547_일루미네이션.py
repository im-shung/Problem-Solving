# 참고: https://reliablecho-programming.tistory.com/110

from collections import deque
import sys
input = sys.stdin.readline

# 육각형 관련한 탐색 문제 나오면, 열2개,행1개 추가해서 배열을 확장하는 사고를 해야 한다.
# 핵심은 회색건물('1')을 탐색하는 것이 아닌 주변 흰색 부분('0')을 탐색한다는 점이다.

w,h = map(int,input().split())
graph = [[0 for _ in range(w+2)] for _ in range(h+2)] # +2씩 해준다. 외밖과 닿는 면을 다 흰색정육각형으로 둘러준다.
for i in range(1, h+1):
    graph[i][1:w+1] = map(int, input().split())

dy = [0, 1, 1, 0, -1, -1]
dx = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]] # 짝수줄, 홀수줄 범위내 이동거리 설정

def bfs(y,x):
    Q = deque([(y,x)])
    visited = [[False]*(w+2) for _ in range(h+2)]
    visited[y][x] = True
    cnt = 0
    
    while Q:
        y,x = Q.popleft()
        
        for i in range(6):
            yy = y + dy[i]
            xx = x + dx[y % 2][i]
            if 0 <= yy < h+2 and 0 <= xx < w+2:
                if graph[yy][xx] == 0 and not visited[yy][xx]:
                    Q.append((yy, xx))
                    visited[yy][xx] = True
                elif graph[yy][xx] == 1:
                    cnt += 1
    return cnt

print(bfs(0,0))