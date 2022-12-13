from collections import deque

LEFT = 6
RIGHT = 2

t = int(input())
queue_list = [deque() for _ in range(t)]

for i in range(t):
    s = list(input())
    for _s in s:
        queue_list[i].append(_s)

k = int(input())
for _ in range(k):
    number, direction = map(int, input().split())
    number -= 1

    dl, dr = direction, direction
    left_list, right_list = [0] * t, [0] * t

    for i in range(t):
        left_list[i] = queue_list[i][LEFT]
        right_list[i] = queue_list[i][RIGHT]

    # 왼쪽 톱니바퀴
    for i in range(number, 0, -1):
        mid = left_list[i]
        left = right_list[i - 1]
        if left != mid:
            dl = -dl
            queue_list[i - 1].rotate(dl)
        else: break

    # 오른쪽 톱니바퀴
    for i in range(number, t - 1, 1):
        mid = right_list[i]
        right = left_list[i + 1]
        if right != mid:
            dr = -dr
            queue_list[i + 1].rotate(dr)
        else: break

    queue_list[number].rotate(direction)


cnt = 0
for _ in range(t):
    if queue_list[_][0] == '1':
        cnt += 1
print(cnt)
