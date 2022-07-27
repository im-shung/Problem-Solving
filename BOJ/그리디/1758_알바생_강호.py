import heapq
n = int(input())
hq = []
for _ in range(n):
    heapq.heappush(hq,-int(input()))
sum = 0
for N in range(1,len(hq)+1):
    M = abs(heapq.heappop(hq))
    money = M-N+1
    if money < 0: money = 0
    sum += money
print(sum)