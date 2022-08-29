from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
ex = deque(enumerate(map(int,input().split())))

result = []
while ex:
    idx,val = ex.popleft()
    print(idx+1,end=" ")
    
    if val > 0:
            ex.rotate(-(val - 1))
    elif val < 0:
        ex.rotate(-val)