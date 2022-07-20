# SW Expert Academy 
# 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg

import sys
sys.stdin = open("../sample_input.txt", "r")

from collections import deque

T = int(input())

def BFS(S,G):
    # 시작점을 큐에 삽입
    queue = deque([(S,0)]) # 큐에 노드와 지난 간선 개수를 함께 저장
    while queue: # 큐가 비어있지 않은 경우
        t, cnt = queue.popleft() # 큐가 첫 번째 원소 반환
        if not visited[t]:
            visited[t] = True # 방문한 곳으로 표시
        for i in group[t]: # t와 연결된 모든 선에 대해
            if not visited[i] and i == G: # 도착 노드라면
                return cnt + 1
            elif not visited[i]: # 방문되지 않은 곳이라면
                queue.append((i,cnt + 1))
    # 도착 노드에 가지 못했다면 0 리턴
    return 0

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    group = [[] for _ in range(V+1)] # 출발 -> 도착 노드 간선 정보 저장 
    visited = [False for _ in range(V+1)] # 노드 방문 여부 저장 [0: 방문 X, 1: 방문 O] 

    for _ in range(E):
        start, end = map(int, input().split()) 
        group[start].append(end)
        group[end].append(start)
        
    S, G = map(int, input().split())  # 경로의 존재를 확인할 출발 노드 S와 도착노드 G
    
    print(f"#{test_case} {BFS(S,G)}")
