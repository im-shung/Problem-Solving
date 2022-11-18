import sys
sys.stdin = open("C:\Program_study\AlgorithmStudy\sample_input.txt", "r")

dr = [1, -1]
dc = [1, -1]

def is_boundary_r(x):
    return x == W or x == 0

def is_boundary_c(y):
    return y == H or y == 0

if __name__ == '__main__':
    W, H = map(int, input().split())
    P, Q = map(int, input().split())
    T = int(input())

    x, y, dist_x, dist_y = P, Q, 0, 0
    for t in range(T):
        x += dr[dist_x]
        y += dc[dist_y]

        if is_boundary_r(x):
            dist_x = (dist_x + 1) % 2

        if is_boundary_c(y):
            dist_y = (dist_y + 1) % 2

    print(x, y)