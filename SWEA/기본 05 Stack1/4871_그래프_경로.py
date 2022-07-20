# SW Expert Academy 
# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVHzyqqe8DFAWg&&

import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

def dfs(S):
    visited[S] = 1
    for i in graph[S]:
        if visited[i] == 0:
            dfs(i)

for test_case in range(1, T+1):
    V, E = map(int, input().split()) # V개의 노드, E개의 간선 
    
    graph = [[] for _ in range(V+1)] # 출발 -> 도착 노드 간선 정보 저장 
    visited = [0 for _ in range(V+1)] # 노드 방문 여부 저장 [0: 방문 X, 1: 방문 O] 
    
    for _ in range(E):
        start, end = map(int, input().split()) 
        graph[start].append(end)
        
    S, G = map(int, input().split())  # 경로의 존재를 확인할 출발 노드 S와 도착노드 G
    
    dfs(S) # DFS 알고리즘 이용 
    
    result = 1
    if visited[G] == 0: # 도착노드 G를 방문하지 않았다면 실패
        result = 0
    print(f"#{test_case} {result}")  