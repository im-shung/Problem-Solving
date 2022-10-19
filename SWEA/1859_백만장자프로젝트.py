for t in range(int(input())):
    n = int(input())
    prices = list(map(int, input().split()))

    benefit = 0
    i = n - 1
    j = n - 2
    while j >= 0:
        if prices[j] < prices[i]:
            benefit += prices[i] - prices[j]
            j -= 1
        elif prices[j] >= prices[i]:
            i = j
            j = i - 1

    print(f'#{t+1} {benefit}')