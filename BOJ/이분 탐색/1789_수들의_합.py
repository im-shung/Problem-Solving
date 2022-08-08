import sys
input = sys.stdin.readline

s = int(input().strip())
n = 1
while (n*(n+1))/2 <= s:
    n += 1
print(n-1)