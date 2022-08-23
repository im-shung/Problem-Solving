import heapq
import sys
sys.stdin = open("sample_input.txt", "r")

n = int(input())
m = int(input())

pi = [[] for _ in range(n+1)]
visitied = [False] * (n+1)
hq = [[0,1]]

for _ in range(m):
    s,e,w = map(int,input().split())
    if s != e:
        pi[s].append([w,e])
        pi[e].append([w,s])

answer = 0
cnt = 0        
while hq:
    if cnt == n:
        break
    w,s = heapq.heappop(hq)
    if not visitied[s]:
        visitied[s] = True
        answer += w
        cnt += 1
        for i in pi[s]:
            heapq.heappush(hq,i)
print(answer)
