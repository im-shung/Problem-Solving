# SW Expert Academy 
# 5255. [파이썬 S/W 문제해결 최적화] 2일차 - 타일 붙이기 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYNNbK29EDFAVT
import sys
sys.stdin = open("../sample_input.txt", "r")

def tiling(N):
    if N == 1: return 1
    elif N == 2: return 3
    elif N == 3: return 6
    else: return tiling(N-1) + 2 * tiling(N-2) + tiling(N-3)

for test_case in range(1, int(input())+1):
    N = int(input())
    
    print(f"#{test_case} {tiling(N)}")