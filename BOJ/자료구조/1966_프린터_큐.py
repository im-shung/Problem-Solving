from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    n,key = map(int,input().split())
    ex = list(map(int,input().split()))
    ex =  deque((v, idx) for idx, v in enumerate(ex))
    cnt = 0
    while True:
        if max(ex)[0] == ex[0][0]:
            cnt += 1
            if ex[0][1] == key:
                print(cnt)
                break
            else:
                ex.popleft()
        else:
            ex.append(ex.popleft())