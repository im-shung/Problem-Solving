# SW Expert Academy 
# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산 D4
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYG3y62EcDFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")      
from collections import deque
 
def bfs(N, M):
    queue = deque()
    queue.append((N, 0))
    visited = set()
    visited.add(N)
    while queue: # 큐가 비어있지 않으면
        cur_node, cnt = queue.popleft()
        for next_node in (cur_node + 1, cur_node - 1, cur_node * 2, cur_node - 10):
            # int(1e6): 100000000
            if next_node <= int(1e6) and next_node not in visited:
                visited.add(next_node)
                queue.append((next_node,cnt+1))
                if next_node == M:
                    return cnt + 1
for test_case in range(1, int(input()) + 1):
    N,M =  map(int, input().split())
    print("#"+str(test_case),bfs(N,M))        