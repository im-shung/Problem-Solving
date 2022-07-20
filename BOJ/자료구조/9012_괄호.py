import sys

for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline()
    S = []
    result = ""
    for val in line:
        if val == '(':
            S.append(val)
        elif val == ')':
            if len(S) == 0: 
                result = "NO"
                break
            elif S.pop() == '(': result = "YES"
    if len(S) != 0: result = "NO"
    print(result)         