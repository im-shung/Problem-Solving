import sys
input = sys.stdin.readline

ex = list(input().strip())
stack = []
cnt = 0
i = 0
while i < len(ex):
    if ex[i] == '(':
        if ex[i+1] == ')':
            cnt += len(stack)
            i += 1
        else:
            stack.append(ex[i])
    elif ex[i] == ')':
        if stack:
            stack.pop()
            cnt += 1
    i += 1
print(cnt)