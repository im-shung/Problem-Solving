N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

mn = 1e9
for i in range(1 << N):
    S, B = 1, 0
    flag = False
    for j in range(N):
        if i & (1 << j):
            flag = True
            S *= arr[j][0]
            B += arr[j][1]
    if flag:
        ans = abs(S-B)
        if mn > ans:
            mn = ans
print(mn)