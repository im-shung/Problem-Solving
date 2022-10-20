from collections import defaultdict

for _ in range(1, int(input()) + 1):
    t = int(input())
    s = list(map(int, input().split()))
    dict = defaultdict()
    for key in s:
        if dict.get(key) is not None:
            dict[key] += 1
        else:
            dict[key] = 1

    mx_key = 0
    mx_value = 0
    for key, value in dict.items():
        if mx_value < value:
            mx_value = value
            mx_key = key
        elif mx_value == value:
            if mx_key < key:
                mx_key = key
    print(f'#{t} {mx_key}')