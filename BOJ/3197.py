# 참고 - https://data-make.tistory.com/625

# 처음 풀이: BFS 2번 진행 -> 시간 초과
    # 1. 모든 좌표를 돌며 빙하를 녹이기 위해 BFS
    # 2. 백조를 찾기 위해 BFS

# 해결 방법: 각각 두 개의 큐를 사용한다.
    # 1. 현재 물 상태인 큐
    # 2. 다음 턴에 물이 될 좌표를 담는 큐

    # 1. 현재 백조가 움직일 수 있는 위치
    # 2. 다음턴에 백조가 움직일 수 있는 위치

import sys
input = sys.stdin.readline # 안 넣으면 시간초과

from collections import deque
import copy

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]

# 한마리 백조는 가만 있고 다른 백조가 이동하며 찾는 순간 끝낸다.
# 빙하 안에 있는 백조는 물 위에 있다.
visited_in = [[False for _ in range(C)] for _ in range(R)]
# 빙하 밖에 있는 백조도 물 위에 있다.
visited_out = [[False for _ in range(C)] for _ in range(R)]

# 두 백조의 위치 정보
swans = []

# 백조가 현재와 다음 날 탐색할 위치를 저장 하는 Queue
swan = deque()
nswan = deque()

# 현재 물 칸과 다음 날 녹을 빙판 위치를 저장 하는 Queue
water = deque()
nwater = deque()

for r in range(R):
    for c in range(C):

        if matrix[r][c] == "L":
            swans.append((r, c))
            matrix[r][c] = "." # 놓칠 수 있는 point. 백조는 물 위에 있다.

        if matrix[r][c] == ".":
            water.append((r, c))

# 1번 백조가 2번 백조를 항해
visited_in[swans[0][0]][swans[0][1]] = True
swan.append(swans[0])

###########################################
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def is_out_range(x, y):
    return not (0 <= x < R and 0 <= y < C)

def printf(arr):
    for a in arr:
        print(''.join(map(str,a)))
    print("-------------------------")

###########################################

def melt():
    # 현재 물 상태에서 BFS를 돌며 X(빙하)를 만나게 되면 다음 턴에 물이 될 좌표이므로 큐에 담습니다.
    while water:
        i, j = water.popleft()
        for _x, _y in list(zip(dr, dc)):
            di, dj = i + _x, j + _y
            # 범위를 초과하거나 이미 방문했을 경우 pass
            if is_out_range(di, dj) or visited_in[di][dj] or visited_out[di][dj]: continue
            # 방문 처리
            visited_out[di][dj] = True
            # 빙하일 경우 다음날 탐색을 위해 큐에 추가
            if matrix[di][dj] == "X":
                # 물 공간과 접촉한 모든 빙판 공간이 녹는다.
                matrix[di][dj] = "."
                nwater.append((di, dj))

def is_meet():
    while swan:
        i, j = swan.popleft()
        for _x, _y in list(zip(dr, dc)):
            di, dj = i + _x, j + _y
            # 범위를 초과하거나 이미 방문했을 경우 pass
            if is_out_range(di, dj) or visited_in[di][dj]: continue
            # 상대 백조를 만났을 경우 return
            if di == swans[1][0] and dj == swans[1][1]: return True
            # 방문 처리
            visited_in[di][dj] = True
            # 빙하일 경우 다음날 탐색을 위해 큐에 추가
            if matrix[di][dj] == "X":
                # 물 공간과 접촉한 모든 빙판 공간이 녹는다.
                matrix[di][dj] = "."
                nswan.append((di, dj))
            else:
                swan.append((di, dj))

    return False

def progress():
    global swan, nswan, water, nwater
    day = 0

    while True:
        # 1. 두 마리의 백조가 만날 수 있는지 확인
        if is_meet():
            break

        # 2. 빙하가 녹는다
        melt()

        swan = copy.deepcopy(nswan)
        nswan = deque()

        water = copy.deepcopy(nwater)
        nwater = deque()

        day += 1

    print(day)

progress()