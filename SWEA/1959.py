def calculate(arr1, arr2, size1, size2):
    global result

    mx = 0
    for i in range(0, size1 - size2 + 1, 1):
        sum = 0
        for x in range(size2):
            sum += arr1[i + x] * arr2[x]
        if sum > mx:
            mx = sum
    result = mx

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0
    if n >= m:
        calculate(A, B, n, m)
    else:
        calculate(B, A, m, n)
    print(f'#{t} {result}')