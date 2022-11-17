dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def is_out_range(x, y):
    return not (1 <= x <= R and 1 <= y <= C)

if __name__ == '__main__':
    C, R = map(int, input().split())
    K = int(input())

    matrix = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
    x, y, dist = R, 1, 0

    flag = False
    for num in range(1, R * C + 1):
        if num == K:
            flag = True
            break
        matrix[x][y] = num
        x += dr[dist]
        y += dc[dist]
        if is_out_range(x, y) or matrix[x][y] != 0:
            x -= dr[dist]
            y -= dc[dist]
            dist = (dist + 1) % 4
            x += dr[dist]
            y += dc[dist]
    if flag:
        print(y, R - x + 1)
    else: print(0)