# 완전탐색 해결법

def change(arr, cnt):
    global result

    tmp = ''.join(map(str, arr))
    if int(tmp) in result[cnt]:
        return
    else:
        result[cnt].append(int(tmp))

    if cnt == 0:
        return

    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            arr[i], arr[j] = arr[j], arr[i]
            change(arr, cnt - 1)
            arr[i], arr[j] = arr[j], arr[i]

for t in range(1, int(input()) + 1):
    arr, cnt = input().split()
    arr = list(arr)
    result = [[] for _ in range(int(cnt) + 1)]
    change(arr, int(cnt))
    print(f'#{t} {max(result[0])}')




# set() 해결법

for tc in range(1, int(input()) + 1):
    data, K = input().split()
    K = int(K)
    N = len(data)
    now = set([data])
    nxt = set()
    for _ in range(K):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1,N):
                    s[i],s[j] = s[j],s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now,nxt = nxt,now

    print('#{} {}'.format(tc,max(map(int,now))))