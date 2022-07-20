# SW Expert Academy 
# 5260. [파이썬 S/W 문제해결 최적화] 3일차 - 부분 집합의 합 D4
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYNxvq3BIDFAVT
# https://swexpertacademy.com/main/talk/solvingTalk/boardCommuView.do?commuId=AXBUZa5quuoDFAVg

import sys
sys.stdin = open("../sample_input.txt", "r")

def find_subset_sum(now_sum, rest_sum, idx):
    global N, K, N_list, cnt

    if now_sum > K: return
    elif now_sum + rest_sum < K: return
    if idx == N:
        if now_sum == K:
            cnt += 1
         # print(result, now_sum)
        return

    rest_sum -= N_list[idx]
    find_subset_sum(now_sum, rest_sum, idx+1)
    now_sum += N_list[idx]
    find_subset_sum(now_sum, rest_sum, idx+1)

for test_case in range(1, int(input())+1):
    N, K = map(int, input().split())
    N_list = [i for i in range(1, N+1)]

    cnt = 0
    find_subset_sum(0, N*(N+1)//2, 0)
    # print(f"#{test_case} {dp(n,k)}")