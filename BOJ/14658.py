import sys
sys.stdin = open("C:\Program_study\AlgorithmStudy\sample_input.txt", "r")

if __name__ == '__main__':
    N, M, L, K = map(int, input().split())
    star = []
    for _ in range(K):
        x, y = map(int, input().split())
        star.append((x, y))

    mx = 0
    for x, _ in star:
        for _, y in star:
            count = 0
            for i, j in star:
                if (x <= i <= x + L) and (y <= j <= y + L):
                    count += 1
            mx = max(mx, count)

    print(K - mx)