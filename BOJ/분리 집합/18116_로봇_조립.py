import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
parent = [i for i in range((10 ** 6)+1)]
cnt = [1 for _ in range((10 ** 6)+1)]

def get_parent(x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent[x])
    return parent[x]    
    
def union(node1,node2):
    a = get_parent(node1)
    b = get_parent(node2)
    if a != b:
        parent[a] = b
        sum = cnt[a] + cnt[b]
        cnt[a] = cnt[b] = sum

for _ in range(n):
    X, *s = map(str,input().split())
    if X == 'I':
        a = int(s[0]); b = int(s[1])
        union(a,b)
    elif X == 'Q':
        c = int(s[0])
        ans = get_parent(c)
        print(cnt[ans])