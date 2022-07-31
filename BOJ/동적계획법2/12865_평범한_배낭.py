import sys
input = sys.stdin.readline

n,k = map(int,input().split())
bag = [0] * (k+1)
    
for _ in range(n):
    w,v = map(int,input().split())
    for i in range(k,w-1,-1):
        pre_v = bag[i]       # 가방에 현재 물건 X
        now_v = v + bag[i-w] # 가방에 현재 물건 O
        bag[i] = max(pre_v,now_v)
print(bag[k]) # 가방무게가 k일 때 물건 최대 가치