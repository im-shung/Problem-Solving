for t in range(1, int(input()) + 1):
    s = list(input())
    idx = 1
    tmp = s[0]

    while idx < len(s):
        if s[idx] == tmp[0]:
            n = len(tmp)
            if ''.join(map(str,s[idx:idx + n])) == tmp:
                break
            else:
                tmp += s[idx]
                idx += 1
        else:
            tmp += s[idx]
            idx += 1
    print(f'#{t} {len(tmp)}')

