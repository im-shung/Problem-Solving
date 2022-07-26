import sys
import math
k = int(sys.stdin.readline().strip())
n = int(math.pow(2, k))
S = list(map(int,sys.stdin.readline().strip().split()))
tree = [0] * n 
cnt = 0
def binary_tree(v): # 중위 순회 (왼쪽 자식) (루트) (오른쪽 자식)
    global cnt
    if v <= n-1:
        binary_tree(v * 2) # (왼쪽 자식)
        tree[v] = S[cnt] # (루트)
        cnt += 1
        binary_tree(v * 2 + 1) # (오른쪽 자식)
binary_tree(1)        
k = 1
while k < n:
    for i in range(k, k*2):
        print(tree[i], end=" ")
    print()
    k *= 2