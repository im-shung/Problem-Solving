import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
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
        if a < b: parent[b] = a
        else: parent[a] = b   

for _ in range(m):
    flag, a, b = map(int,input().split())
    if flag == 0:
        union(a,b)
    elif flag == 1:
        if get_parent(b) == get_parent(a):
            print("YES")
        else: print("NO")