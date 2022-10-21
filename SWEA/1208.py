for t in range(1, 11):
    n = int(input())
    s = list(map(int, input().split()))

    cnt, mx, mn = 0, 0, 0
    while cnt <= n:
        cnt += 1
        mx, mn = max(s), min(s)
        if mx - mn <= 1:
            break
        mx_index = list(filter(lambda x: s[x] == mx, range(100)))
        mn_index = list(filter(lambda x: s[x] == mn, range(100)))
        s[mx_index[0]] -= 1
        s[mn_index[0]] += 1
    print(f'#{t} {mx - mn}')