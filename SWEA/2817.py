for t in range(1, int(input())+ 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    result = 0

    # 2^N개의 부분집합 돌기, 부분집합은 idx로 구성
    for i in range(1 << n):
        sub_sum = 0
        # N개의 수열 돌기
        for j in range(n): # N개의 수
            if i & (1 << j): # 부분집합 i가 j 인덱스를 가지고 있으면
                sub_sum += arr[j] # arr[j]를 더한다.
        if sub_sum == k:
            result += 1

    print(f'#{t} {result}')
