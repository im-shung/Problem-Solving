import sys
import heapq
N = int(sys.stdin.readline().strip())
hq = [] 
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if len(hq) == 0: print(0)
        else: print(abs(heapq.heappop(hq))) # O(log n)
    else: heapq.heappush(hq, -x) # heapq는 최소힙만 다루기 때문에 최대힙으로 구현하기 위해 -부호 붙여 push한다