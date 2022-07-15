# SW Expert Academy 
# 5263. [파이썬 S/W 문제해결 최적화] 4일차 - 그래프 최소 비용 D4
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYODN63DsDFAVT
## 10개의 테스트케이스 중 9개가 맞았습니다.
import sys
sys.stdin = open("../sample_input.txt", "r")

# D[i][j]: i에서 j로 가는 최단 경로 가중치 합
# 최초 D[i][j]에는 간선 (i,j)의 가중치 저장, i에서 j로 간선이 없으면 INF

def all_pair_shortest():
    for k in range(n): # 경우 가능한 정점을 0 .. n-1 으로 확장
        for i in range(n): # 모든 정점 쌍 (단, i != k) 
                for j in range(n): #(단 j != k, j != i)
                        D[i][j] = min(D[i][k] + D[k][j], D[i][j])
for test_case in range(1, int(input())+1):
    n = int(input())
    D = [[100 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(len(arr)):
            if arr[j] == 0:
                D[i][j] = 100
            else: D[i][j] = arr[j]
    all_pair_shortest()
    max = 0
    for i in range(n):
        for j in range(n):
            if D[i][j] != 100:
                if D[i][j] > max:
                    max = D[i][j]
    # print(D)
    print(f"#{test_case} {max}")