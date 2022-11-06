def change1(num):
    for i, val in enumerate(s):
        if (i+1) % num == 0:
            if val: s[i] = 0
            else: s[i] = 1

def change2(num):
    if s[num - 1]: s[num - 1] = 0
    else: s[num - 1] = 1

    if num == 1 or num == n:
        return

    left, right = num - 2, num
    while left >= 0 and right < n:
        result = s[left] + s[right]
        if result == 2:
            s[left] = 0
            s[right] = 0
        elif result == 0:
            s[left] = 1
            s[right] = 1
        else: break

        left -= 1
        right += 1

def prinf(arr):
    for i in range(0, len(arr), 20):
        print(' '.join(map(str,arr[i:i+20])))

if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))
    m = int(input())

    for _ in range(m):
        x, num = map(int, input().split())
        if x == 1: change1(num)
        elif x == 2: change2(num)

    prinf(s)