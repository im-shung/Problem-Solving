# SW Expert Academy 
#5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYFsQq11kDFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")      
      
T = int(input())

def quick_sort(A,l,r):
    if l < r:
        s = partition(A,l,r)
        quick_sort(A,l,s-1)
        quick_sort(A,s+1,r)

def partition(A,l,r):
    p = A[l]
    i = l + 1
    j = r
    while i <= j:
        while(i<=j and A[i] <= p): i+= 1
        while(i<=j and A[j] >= p): j-= 1
        if i<= j:
            A[i],A[j] = A[j],A[i]
    A[l],A[j] = A[j], A[l]
    return j 

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr,0,len(arr)-1)
    print(f"#{test_case} {arr[len(arr)//2]}") 