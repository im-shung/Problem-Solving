from collections import deque

# 모든 작업이 완료되는 것은 작업 시간 중에 가장 오래 걸리는 것이 완료 되었을 때이다.
# 즉 자신의 우선순위에 있는 작업 중에 가장 오래 걸리는 작업에 자신의 작업시간을 더한 값

n = int(input())
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
indegree = [0] * (n+1)

def sort():
    Q = deque()
    result = [0] * (n+1)
    for i in range(1,n+1):
        if indegree[i] == 0:
            Q.append(i)
            result[i] = time[i] # 놓쳤던 point1
    while Q:
        x = Q.popleft()
        for i in graph[x]:
            result[i] = max(result[i],result[x]+time[i])  # 놓쳤던 point2
            indegree[i] -= 1
            if indegree[i] == 0:
                Q.append(i)
    print(max(result))

for i in range(1,n+1):
    s = list(map(int,input().split()))
    time[i] = s[0]
    if s[1] > 0:
        for j in s[2:]:
            graph[j].append(i)
            indegree[i] += 1
sort()