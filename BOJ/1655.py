import heapq
import sys
input = sys.stdin.readline # 안 넣으면 시간초과


n = int(input())
A = [] # 최대힙
B = [] # 최소힙
for i in range(n):
    number = int(input())

    if len(A) == len(B):
        heapq.heappush(A, -number)
    else:
        heapq.heappush(B, number)

    if not B:
        print(-A[0])
        continue
    if -A[0] > B[0]:
        m = -heapq.heappop(A)
        n = heapq.heappop(B)

        heapq.heappush(A, -n)
        heapq.heappush(B, m)

    print(-A[0])
