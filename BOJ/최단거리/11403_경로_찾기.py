from collections import deque
import sys
# input = sys.stdin.readline
sys.stdin = open("sample_input.txt", "r")

n = int(input())

graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    s = list(map(int,input().split()))
    for j in range(n):
        if s[j] == 1:
            graph[i].append((j+1))

def find_node(n):
    memo = []
    visited = []
    Q = deque([n])
    while Q:
        x = Q.popleft()
        for i in graph[x]:
            if not i in visited:
                memo.append(i)
                visited.append(i)
                Q.append(i)
    return memo    
    
for i in range(1,n+1):
    memo = find_node(i)
    for j in range(1,n+1):
        if j in memo:
            print(1, end=" ")
        else: print(0, end=" ")
    print()