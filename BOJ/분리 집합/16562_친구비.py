from collections import deque
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
cost = deque(map(int,input().split()))
cost.appendleft(0)
parent = [i for i in range(n+1)]

#부모 노드의 값을 얻는 함수
def get_parent(x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent[x])
    return parent[x]    

#두 부모 노드를 합치는 함수
def union(node1,node2):
    a = get_parent(node1)
    b = get_parent(node2)
    if a != b:
        # 친구관계를 형성할 때, root를 비용이 적은 친구로 한다.
        if cost[a] <= cost[b]: parent[b] = a
        else: parent[a] = b

for _ in range(m):
    v, w = map(int,input().split())
    union(v,w)

result = 0
for idx, root in enumerate(parent):
    if idx == root:
        result += cost[idx]

if result > k: print("Oh no")
else: print(result)