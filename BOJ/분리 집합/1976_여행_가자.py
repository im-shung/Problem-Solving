import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

def get_parent(x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent[x])
    return parent[x]   

def union(node1,node2):
    a = get_parent(node1)
    b = get_parent(node2)
    if a != b:
        if a < b: parent[b] = a
        else: parent[a] = b

for i in range(1,n+1):
    s = list(map(int,input().split()))
    for j in range(len(s)):
        if s[j] == 1: # 연결 
            union(i,j+1)
plan = list(map(int,input().split()))

result = []
for i in plan:
    result.append(get_parent(i))
    
if len(set(result)) == 1: # 두 도시가 연결되어 있다면 같은 요소가 입력되어 len이 1
    print("YES")
else:
    print("NO")