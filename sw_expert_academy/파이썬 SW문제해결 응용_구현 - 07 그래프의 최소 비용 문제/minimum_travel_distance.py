# SW Expert Academy 
# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리 D4
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYHO7a2JoDFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")      

import math
INF = math.inf

def Dijkstra(r): 								
    D = [INF] * N 						       
    P = [None] * N 								
    visited = [False] * N	 					
    D[r] = 0							
    
    for _ in range(N):			 					
        min_index = -1
        min = INF
        for i in range(N):
            if not visited[i] and D[i] < min: 	
                min = D[i]
                min_index = i
        visited[min_index] = True 					
        for v, val in G[min_index]: 				
            if not visited[v] and D[min_index] + val < D[v]: 	
                D[v] = D[min_index] + val 						
                P[v] = min_index 				
    return D[-1]
for test_case in range(1, int(input()) + 1):
    V,E =  map(int, input().split())
    N = V + 1
    G = [[] for _ in range(E)]
    for _ in range(E):
        index, v, val = map(int, input().split())
        G[index].append((v,val))
    print(f"#{test_case} {Dijkstra(0)}")  