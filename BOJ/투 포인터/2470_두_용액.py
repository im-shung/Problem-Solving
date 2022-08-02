import sys  
# input = sys.stdin.readline
sys.stdin = open("sample_input.txt", "r")

n = int(input())
A = list(map(int,input().split()))
A.sort(key = lambda x: abs(x))
# print(A)
result = 200001
x=0;y=0
l = 1; r = n-1
tag = 0
while l<=r:
    if tag == 0:
        if abs(A[l-1] + A[l]) < result:
            result = abs(A[l-1] + A[l])
            x = A[l-1]; y = A[l]
        l +=1
        tag = 1
    if tag == 1: 
        if abs(A[r] + A[r-1]) < result:
            result = abs(A[r] + A[r-1])
            x = A[r]; y = A[r-1]
        r -= 1
        tag = 0
tmp = []
tmp.append(x);tmp.append(y)
tmp.sort()
print(*tmp)