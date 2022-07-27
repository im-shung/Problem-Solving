import sys
A, B, C, M = map(int,sys.stdin.readline().strip().split())
pirodo = 0
day = 24
work = 0
while day > 0:
    day -= 1
    if A > M: break
    elif pirodo + A > M:
        pirodo -= C
        if pirodo < 0: pirodo = 0
    else:
        pirodo += A
        work += B
print(work)