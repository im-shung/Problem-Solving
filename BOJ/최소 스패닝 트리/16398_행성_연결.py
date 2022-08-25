import heapq
import sys
sys.stdin = open("sample_input.txt", "r")

n = int(input())
parent = [i for i in range(n+1)]
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

for i in range(1,n+1):
    w = list(map(int,input().split()))
    for j in range(1,n+1):
        if i != j:
            pi.append((w[j-1],i,j))
           
pi.sort()

answer = 0
for w,s,e in pi:
    if find_parent(s) != find_parent(e):
        union_parent(s,e)
        answer += w

print(answer)