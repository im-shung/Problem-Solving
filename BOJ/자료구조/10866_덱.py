import sys
from collections import deque
D = deque()
for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline().split()
    cmd = line[0]
    if cmd == "push_back":
        D.append(line[1])
    elif cmd == "push_front":
        D.appendleft(line[1])
    elif cmd == "pop_front":
        if len(D) == 0: print(-1)
        else: print(D.popleft())
    elif cmd == "pop_back":
        if len(D) == 0: print(-1)
        else: print(D.pop())
    elif cmd == "size":
        print(len(D))
    elif cmd == "empty":
        if len(D) == 0: print(1)
        else: print(0)
    elif cmd == "front":
        if len(D) == 0: print(-1)
        else: print(D[0])
    elif cmd == "back":
        if len(D) == 0: print(-1)
        else: print(D[-1])