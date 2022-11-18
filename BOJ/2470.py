import sys
input = sys.stdin.readline

# L = "남아있는 것들 중" 제일 작은 원소
# R = "남아 있는 것들 중" 제일 큰 원소
# 1. 최소 + 최대 < 0
    # 최소 입장에서는 최선책을 만난 상태! 짝을 찾았으니 삭제(더 고려 X)
# 2. 최소 + 최대 > 0
    # 최대 입장에서는 최선책을 만난 상태! 짝을 찾았으니 삭제(더 고려 X)

if __name__ == '__main__':
    n = int(input())
    a = sorted(list(map(int, input().split())))

    L, R = 0, n - 1
    v1, v2, best_sum = 0, 0, 1 << 31 # MAX_VALUE

    while L < R:
        if best_sum > abs(a[L] + a[R]):
            best_sum = abs(a[L] + a[R])
            v1, v2 = a[L], a[R]
        if a[L] + a[R] > 0:
            R -= 1
        else:
            L += 1
    print(v1, v2)