from collections import defaultdict

if __name__ == '__main__':
    n = int(input())
    pair = defaultdict(int)
    pair[0] = 5; pair[5] = 0
    pair[1] = 3; pair[3] = 1
    pair[2] = 4; pair[4] = 2

    dice = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for num in range(1, 7):
        sub_result = 0
        key = num
        for i in range(n):
            key_idx = dice[i].index(key)
            next_key = dice[i][pair[key_idx]]

            max_val = 0
            for x, val in enumerate(dice[i]):
                if x == key_idx or x == pair[key_idx]:
                    continue
                if max_val < val:
                    max_val = val
                max_val = max(max_val, val)
            sub_result += max_val
            key = next_key
        result = max(result, sub_result)
    print(result)