from collections import deque
import sys
sys.stdin = open("sample_input.txt", "r")

input = sys.stdin.readline

m = int(input().strip())
n = int(input().strip())
result = deque()
sum = 0
for value in range(m,n+1):
    if value == 1: continue
    for x in range(2,value):
        if value % x == 0:
            break
    else:
        result.append(value) 
        sum += value   
if len(result) == 0:
    print(-1)
else:
    print(sum)    
    print(result.popleft())