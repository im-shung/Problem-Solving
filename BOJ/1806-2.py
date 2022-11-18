import sys
input = sys.stdin.readline

# 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램

if __name__ == '__main__':
    n, S = list(map(int, input().split()))
    a = list(map(int, input().split()))
    R = -1
    sum = 0
    ans = n + 1

    for L in range(n):
        # R을 옮길 수 있을 때 까지 옮기기
        while R + 1 < n and sum < S:
            R += 1
            sum += a[R]

        # [L ... R] 의 합, 즉 sum이 조건을 만족하면 정답 갱신하기
        if sum >= S:
            ans = min(ans, R - L + 1)

        # L - 1을 구간에서 제외하기
        sum -= a[L]

    # ans 값을 보고 불가능 판단하기
    if ans == n + 1:
        ans = 0
    print(ans)