import heapq
import sys
sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline

hq = []
for idx in range(int(input().strip())):
    heapq.heappush(hq,-int(input().strip()))
sum = 0
while len(hq) > 0:
    if len(hq) >= 3:
       sum += -heapq.heappop(hq) + -heapq.heappop(hq)
       heapq.heappop(hq)
    else:
        sum += -heapq.heappop(hq)
print(sum)