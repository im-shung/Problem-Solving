for t in range(1, 11):
    n = int(input())
    h_list = list(map(int,input().split()))
    sum = 0
    for i in range(2, n - 2):
        left = max(h_list[i - 1], h_list[i - 2])
        right = max(h_list[i + 1],h_list[i + 2])
        mid = max(left, right)

        if mid > h_list[i]:
            continue
        sum += h_list[i] - mid
    print(f'#{t} {sum}')