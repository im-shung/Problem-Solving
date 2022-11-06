def brute_force(x1, x2):
    val = x2
    cnt = 1
    while x2 >= 0:
        x1, x2 = x2, x1 - x2
        cnt += 1
    return cnt, val

n = int(input())

cnt, n2 = 0, 0
for m in range(1, n + 1):
    _cnt, _n2 = brute_force(n, m)

    if cnt < _cnt:
        cnt = _cnt
        n2 = _n2

print(cnt)
print(n, end = " ")
while n2 >= 0:
    n, n2 = n2, n - n2
    print(n, end = " ")