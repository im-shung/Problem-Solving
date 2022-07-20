# SW Expert Academy 
# 5262. [파이썬 S/W 문제해결 최적화] 4일차 - 정렬된 부분 집합 D4
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYODN63DsDFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")

from bisect import bisect_left

def LIS_DP():
    LIS = [1]
    C = [a[0]]
    
    for i in range(1, n):
        if a[i] > C[-1]: # 현재 값이 배열의 마지막 값보다 큰 경우
            C.append(a[i])
            LIS.append(LIS[-1] + 1)
        else: # 그렇지 않은 경우
            idx = bisect_left(C,a[i]) # 이진 검색: 정렬된 순서를 유지하도록 C에 a[i]를 삽입할 위치를 리턴
            C[idx] = a[i]
    return len(C)

for test_case in range(1, int(input())+1):
    n, *a = map(int, input().split())
    print(f"#{test_case} {LIS_DP()}")