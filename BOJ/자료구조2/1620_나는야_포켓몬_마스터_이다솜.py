import sys
N,M = map(int,input().split())
key = {}
value = {}
for i in range(1,N+1):
    T = sys.stdin.readline().strip()
    key[i] = T
    value[T] = i
for _ in range(M):
    q = sys.stdin.readline().strip()
    if q.isdigit(): # q가 모두 숫자로 이루어져 있으면
        print(key[int(q)])
    else:
        print(value[q])