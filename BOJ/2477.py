if __name__ == '__main__':
    k = int(input())
    d = []
    for _ in range(6):
        a,b = map(int, input().split())
        d.append([a,b])

    sub, ans = 0, 0
    for x in range(6):
        if d[x%6][0] == d[(x+2)%6][0] and d[(x+1)%6][0] == d[(x+3)%6][0]:
            sub = d[(x+1)%6][1] * d[(x+2)%6][1]
            ans = d[(x+4)%6][1] * d[(x+5)%6][1]
            break
    print((ans - sub) * k)