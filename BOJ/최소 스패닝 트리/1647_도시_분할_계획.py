import sys
sys.stdin = open("sample_input.txt", "r")

v,e = map(int,input().split())
parent = [i for i in range(v+1)]
pi = []

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(e):
    s,e,w = map(int,input().split())
    pi.append((w,s,e))

pi.sort()

answer = 0
max = 0
for w,s,e in pi:
    if find_parent(s) != find_parent(e):
        union_parent(s,e)
        answer += w
        if max < w:
            max = w
print(answer-max)