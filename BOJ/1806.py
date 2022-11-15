import sys

if __name__ == '__main__':
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    tmp = 0
    cnt = 0
    mn = sys.maxsize

    for i in range(n):
        tmp += arr[i]  # 현재 인덱스의 값을 더한다.
        cnt += 1
        if tmp >= s: # 만약 s를 넘는다면
            for j in range(i - cnt + 1, i, 1): # 더했던 인덱스들을 차례로 빼본다.
                if tmp - arr[j] >= s: # 만약 전의 인덱스를 빼고도 s를 넘는다면, 해당 인덱스 제외 (cnt, tmp 감소)
                    tmp -= arr[j]
                    cnt -= 1
                else: break
            mn = min(mn, cnt)

    if mn == sys.maxsize: print(0)
    else: print(mn)