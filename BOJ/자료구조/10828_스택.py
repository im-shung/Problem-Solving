import sys

S = []
for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline().split()
    if line[0] == "push": 
        S.append(line[1])
    elif line[0] == "pop": 
        if len(S) == 0: print(-1)
        else: print(S.pop())
    elif line[0] == "size": 
        print(len(S))
    elif line[0] == "empty": 
        if len(S) == 0: print(1)
        else: print(0)
    elif line[0] == "top": 
        if len(S) == 0: print(-1)
        else: print(S[-1])