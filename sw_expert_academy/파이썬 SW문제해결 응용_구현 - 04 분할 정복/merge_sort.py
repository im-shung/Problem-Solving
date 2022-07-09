# SW Expert Academy 
# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYFsQq11kDFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")      
      
T = int(input())

def merge_sort(m):
    if len(m) <=1: return m
    
    # 분할하기
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)

def merge(left,right):
    global cnt
    if left[-1] > right[-1]: # 병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.
        cnt += 1
        
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print(f"#{test_case} {arr[len(arr)//2]} {cnt}") #정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다.
    



