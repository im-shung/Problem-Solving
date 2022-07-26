import sys
import heapq
N = int(sys.stdin.readline().strip())
hq = []
for _ in range(N):
    for i in list(sys.stdin.readline().split()):
        heapq.heappush(hq,int(i))
        if len(hq) > N: # 메모리 초과 방지
            heapq.heappop(hq)
print(min(hq))