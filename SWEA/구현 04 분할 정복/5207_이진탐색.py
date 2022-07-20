# SW Expert Academy 
# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYFsQq11kDFAVT
# 시간초과로 다시 풀어야함

import sys
sys.stdin = open("../sample_input.txt", "r")      
      
T = int(input())

def binary_search(A,l,r,key):
    global cnt
    m = (l + r) // 2 
    if not key in A: return
    if A[m] == key: 
        cnt += 1
        return
    elif A[m] < key:
        binary_search(A,m+1,r,key)
    elif A[m] > key:
        binary_search(A,l,m-1,key)
         
for test_case in range(1, T+1):
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in B:
        binary_search(A,0,len(A)-1,i)
    print(f"#{test_case} {cnt}")
        