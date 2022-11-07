if __name__ == '__main__':
    width, height = map(int, input().split())
    w_arr = []
    h_arr = []

    for _ in range(int(input())):
        a, n = map(int, input().split())
        if a: h_arr.append(n)
        else: w_arr.append(n)
    w_arr.append(height); h_arr.append(width)
    w_arr.sort(); h_arr.sort()

    x, y = 1, 1
    mx = 0
    for w in w_arr:
        for h in h_arr:
            mx = max((w - x + 1) * (h - y + 1), mx)
            y = h + 1
        x = w + 1
        y = 1

    print(mx)
