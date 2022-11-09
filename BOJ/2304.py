n = int(input())
s = []
for _ in range(n):
    L, H = map(int,input().split())
    s.append([-H, L])
s.sort()
result = -s[0][0]
l_s, r_s = 0, 0

mid = s[0][1]
l, r = mid, mid
for i in range(1, n):
    H, L = s[i]
    if L > r:
        r_s = abs(L - r)
        result += -H * r_s
        r = L
    elif L < l:
        l_s = abs(L - l)
        result += -H * l_s
        l = L
print(result)
