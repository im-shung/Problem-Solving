import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]

def pooling(n,x,y):
    half = n//2
    if n == 2:
        arr = [A[x][y],A[x+1][y],A[x][y+1],A[x+1][y+1]]
        arr.sort()
        return arr[-2]
    l_t = pooling(half, x, y)
    r_t = pooling(half, x + half, y)
    l_b = pooling(half, x, y + half)
    r_b = pooling(half, x + half, y + half)
    arr = [l_t, r_t, l_b, r_b]
    arr.sort()
    return arr[-2]
print(pooling(n,0,0))