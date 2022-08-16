from collections import deque
import sys
input = sys.stdin.readline

def find_w_time():
    Q = deque()
    result = [0] * (n+1)
    for i in range(1,n+1):
        if indegree[i] == 0:
            Q.append(i)
            result[i] = time[i]
    while Q:
        x = Q.popleft()
        if x == w:
            return result[x]
        for i in graph[x]:
            result[i] = max(result[i],result[x]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                Q.append(i)

for _ in range(int(input().strip())):
    n,k = map(int,input().split())
    time = [0]
    time.extend(list(map(int,input().split())))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(k):
        i,j = map(int,input().split())
        graph[i].append(j)
        indegree[j] += 1
    w = int(input()) # 건물 w를 건설완료 하는데 드는 최소 시간 출력하는 문제
    print(find_w_time())