import sys
from collections import deque

D = deque()
for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline().split()
    if line[0] == "push": D.append(line[1])
    elif line[0] == "pop" :
        if len(D) == 0: print(-1)
        else: print(D.popleft())
    elif line[0] == "size" : print(len(D))
    elif line[0] == "empty" :
        if len(D) == 0: print(1)
        else: print(0)
    elif line[0] == "front" :
        if len(D) == 0: print(-1)
        else: print(D[0])
    elif line[0] == "back" :
        if len(D) == 0: print(-1)
        else: print(D[-1])