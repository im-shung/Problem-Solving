import heapq
import sys
sys.stdin = open("sample_input.txt", "r")

v,e = map(int,input().split())
pi = [[] for _ in range(v+1)]
visitied = [False] * (v+1)
hq = [[0,1]]

for _ in range(e):
    s,e,w = map(int,input().split())
    pi[s].append([w,e])
    pi[e].append([w,s])

answer = 0
cnt = 0
while hq:
    if cnt == v: 
        break
    w,s = heapq.heappop(hq)
    if not visitied[s]:
        visitied[s] = True
        answer += w
        cnt += 1
        for i in pi[s]:
            heapq.heappush(hq,i)
print(answer)