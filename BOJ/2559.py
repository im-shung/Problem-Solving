if __name__ == '__main__':
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    result = sum(s[:k])
    mx = result
    for i in range(0, n - k):
        sub = result - s[i] + s[i + k]
        if mx < sub:
            mx = sub
        result = sub
    print(mx)