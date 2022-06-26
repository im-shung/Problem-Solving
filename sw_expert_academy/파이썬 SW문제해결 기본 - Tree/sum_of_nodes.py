# SW Expert Academy 
# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg

import sys
sys.stdin = open("../sample_input.txt", "r")

T = int(input())

def node_search(v):
    cnt = 0
    if v <= N:
        node_search(v + 1)
        
        parent = v//2
        if parent >= 1 and tree[parent] == 0:
            if v == N: # 마지막 노드이면 
                cnt = tree[v]
            if v+1 <= N and (v+1)// 2 == parent :
                cnt = tree[v] + tree[v+1]
            elif (v-1)// 2 == parent : 
                cnt = tree[v] + tree[v-1]
            
            tree[parent] = cnt
            return

for test_case in range(1, T+1):
    N, M, L = map(int, input().split()) # 노드의 개수 N, 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    tree = [0] * (N+1)
    node_list = list()
    for _ in range(M):
        node, value = map(int, input().split())
        node_list.append(node)
        tree[node] = value # 리프 노드 삽입
    cnt = 1
    node_search(1)
    print(f"#{test_case} {tree[L]}")