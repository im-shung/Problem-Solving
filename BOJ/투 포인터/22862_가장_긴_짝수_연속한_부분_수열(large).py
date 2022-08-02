import sys
sys.stdin = open("sample_input.txt", "r")
# input = sys.stdin.readline

n,k = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
l, r = 0,0
cnt = 0
while r < n:
    if A[r] % 2 != 0:
        cnt += 1
    if cnt > k:
        ans = max(ans, r - l - k)
        cnt = 0
        l += 1
        r = l
    else:
        r += 1
print(ans)