import sys
sys.stdin = open("C:\Program_study\AlgorithmStudy\sample_input.txt", "r")

input = sys.stdin.readline

# sliding window 알고리즘 - O(n + k) 풀이
# 연속해서 먹는 접시 = sliding window(길이는 k)를 설정하고, 이를 한 칸씩 움직이면서 최대 먹을 수 있는 초밥의 종류를 얻으면 끝!
# i번 초밥이 현재 보고 있는 접시의 범위 내에서 몇 개가 있는지를 저장하는 배열을 하나 둔다.(kind)
# 현재 초밥의 종류의 개수를 tot라는 변수에 저장해두고
# 초밥의 추가/삭제를 kind값을 1 증가/1 감소하는 것으로 처리한다.
# 이 때 이전에 없던 초밥(kind=0)이 추가되거나 이전에 단 1개 있던(kind=1) 초밥이 제거될 경우 tot를 1 증가/1 감소 시킵니다.

if __name__ == '__main__':
    N, D, K, C = map(int, input().split())
    S = []
    for _ in range(N):
        S.append(int(input()))

    kind = [0 for _ in range(D + 1)]
    tot = 0

    # 처음 K개 초기화
    for i in range(N - K, N):
        if kind[S[i]] == 0:
            tot += 1
        kind[S[i]] += 1

    # 이후 sliding window 알고리즘으로 회전
    mx = 0
    for i in range(N): # (처음 순서: 0번 초밥 추가, 4번 초밥 제거)
        # 초밥 추가
        if kind[S[i]] == 0:
            tot += 1
        kind[S[i]] += 1

        # 초밥 제거
        del_dish = (i - K) % N
        print(i, del_dish)
        if kind[S[del_dish]] == 1:
            tot -= 1
        kind[S[del_dish]] -= 1

        # 최대 먹을 수 있는 초밥의 종류
        mx = max(mx, tot + (kind[C] == 0))
    print(mx)