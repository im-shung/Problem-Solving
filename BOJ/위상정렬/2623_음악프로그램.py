from collections import deque
import sys
sys.stdin = open("sample_input.txt", "r")

# input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

def sort():
    Q = deque()
    result = [(0,0)] * (n+1)
    for i in range(1,n+1):
        if indegree[i] == 0:
            result[i] = (1,i)
            Q.append(i)
    while Q:
        x = Q.popleft()
        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                result[i] = (result[x][0]+1,i)
                Q.append(i) 
    result.sort()
    print('\n'.join(str(result[i][1]) for i in range(1,n+1)))    

for _ in range(m):
    m, *s = list(map(int,input().split()))
    for i in range(m-1):
        graph[s[i]].append(s[i+1])
        indegree[s[i+1]] += 1
sort()