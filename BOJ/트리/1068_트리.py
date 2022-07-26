import sys
sys.stdin = open("sample_input.txt", "r")
n = int(sys.stdin.readline().strip())
graph = list(map(int, sys.stdin.readline().strip().split())) # S: 0번 노드부터 N-1번 노드까지, 각 노드의 부모
del_node = int(sys.stdin.readline().strip())
tree = [0] * n
visited = [False] * n
cnt = 0
def dfs(v):
    global cnt
    if v == del_node: return
    for i in range(n):
        if v == graph[i]:
            visited[v] = True
            dfs(i)
    else: 
        if visited[v] == False:
            cnt += 1
dfs(0)
print(cnt)