import sys
input = sys.stdin.readline

n = int(input())
ex = list(map(int,input().split()))
ex.sort()
if n % 2 != 0:
    ex = [0] + ex
max = 0
for i in range(len(ex)//2):
    sum = ex[i]+ex[len(ex)-1-i]
    if max < sum:
        max = sum
print(max)    