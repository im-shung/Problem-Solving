import sys
import heapq
sys.stdin = open("sample_input.txt","r")
N = int(sys.stdin.readline().strip())
hq = []
for _ in range(N):
    s = list(sys.stdin.readline().split())
    for i in range(N):
        heapq.heappush(hq,int(s[i]))
print(heapq.nlargest(N,hq)[-1])