# SW Expert Academy 
# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg

import sys
sys.stdin = open("../sample_input.txt", "r")

T = int(input())

def binary_heap(v):
    if v <= N:
        heap.append(number[v]) # 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
        m = v
        while m >= 2:
            while heap[m] < heap[m//2]: # 자식 노드가 부모 노드보다 작으면
                heap[m],heap[m//2] = heap[m//2], heap[m] # 자리를 바꾼다
            m = m//2
        binary_heap(v+1)
       
        
for test_case in range(1, T+1):
    N = int(input()) 
    number = list(map(int, input().split()))
    number = [0] + number
    
    heap = list(); heap.append(0) # 0인덱스는 미리 초기화
    
    binary_heap(1)
    
    # 마지막 노드의 조상 노드에 저장된 정수의 합 구하기
    result = 0
    while N >= 1:
        result += heap[N//2]
        N = N//2
    print(f"#{test_case} {result}")
