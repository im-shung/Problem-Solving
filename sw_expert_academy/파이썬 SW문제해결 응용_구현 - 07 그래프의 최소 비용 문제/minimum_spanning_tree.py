# SW Expert Academy 
# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리 D4
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYHO7a2JoDFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")      

import math
INF = math.inf

def MST_PRIM(s): 									# G: 그래프, s: 시작 정점
    key = [INF] * N 						        # 1. 가중치를 무한대로 초기화
    pi = [None] * N 								# 2. 트리에서 연결될 부모 정점 초기화
    visited = [False] * N	 						# 3. 방문 여부 초기화
    key[s] = 0 										# 4. 시작 정점의 가중치를 0으로 설정
    
    for _ in range(N):			 					# 5. 정점의 개수만큼 반복
        min_index = -1
        min = INF
        for i in range(N):
            if not visited[i] and key[i] < min: 	# 6. 방문 안한 정점 중 최소 가중치 정점 찾기
                min = key[i]
                min_index = i
        visited[min_index] = True 					# 7. 최소 가중치 정점 방문처리
        for v, val in G[min_index]: 				# 8. 선택 정점의 인접한 정점
            if not visited[v] and val < key[v]: 	# 9
                key[v] = val 						# 10. 가중치 갱신
                pi[v] = min_index 					# 11. 트리에서 연결될 부모 정점
    return sum(key)
for test_case in range(1, int(input()) + 1):
    V,E =  map(int, input().split())
    N = V+1 # 정점의 개수 
    G = [[] for _ in range(N)]
    for _ in range(E):
        index, v, val = map(int, input().split())
        G[index].append((v,val))
        G[v].append((index,val)) # 중요! 무향 그래프이기 때문에 이것도 꼭 넣어줘야 함 
    print(f"#{test_case} {MST_PRIM(0)}")  