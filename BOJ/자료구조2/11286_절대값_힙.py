import sys
import heapq
N = int(sys.stdin.readline().strip())
hq = []
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if len(hq) == 0: print(0)
        else: print(heapq.heappop(hq)[1])
    else: heapq.heappush(hq,(abs(x),x)) # heapq는 tuple로 구성 시 맨 앞 숫자만 가지고 정렬한다.