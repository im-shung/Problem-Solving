import sys
input = sys.stdin.readline

n, k = map(int,input().split())
A = list(map(int,input().split()))
answer = 0
cnt = [0] * 10001
l = 0
for r in range(n):
    cnt[A[r]] += 1
    while cnt[A[r]] > k:  # count[idx]가 k와 같은 경우, k보다 작아질 때까지 left를 오른쪽으로 이동시킨다.
        cnt[A[l]] -= 1
        l += 1
    answer = max(answer, r - l + 1)
print(answer)