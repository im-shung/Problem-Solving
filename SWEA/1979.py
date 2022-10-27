def get_cnt(arr):
    answer = 0
    for i in range(n):
        memo = []
        cnt = 0
        for j in range(n):
            if arr[i][j]: # 1이면 cnt 1 증가
                cnt += 1
            else: # 0이면 cnt = 0으로 초기화
                if cnt: memo.append(cnt)
                cnt = 0

        if arr[i][-1]: # 마지막 cnt 넣어주기
            memo.append(cnt)

        for a in memo:
            if a == k: # 1이 k번 연속하는지 검사
                answer += 1
    return answer

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]

    result = 0

    # 가로
    result += get_cnt(matrix)

    # 세로
    vertical_matrix = list(map(list, zip(*matrix[::-1])))
    result += get_cnt(vertical_matrix)

    print(f'#{t} {result}')