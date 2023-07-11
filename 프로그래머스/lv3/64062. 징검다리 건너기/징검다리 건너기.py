from heapq import heappush, heappop

def solution(stones, k):
    heap = [] # val, idx 순서로 저장
    
    i = 0
    for i in range(k): 
        heappush(heap, [-stones[i], i]) # 최대힙이라 부호 바꿔서 push
    
    answer = -heap[0][0]
    i+=1
    
    while i < len(stones):
        heappush(heap, [-stones[i], i])
        i+=1
        while heap[0][1] < i-k:
            heappop(heap)
        answer = min(answer, -heap[0][0])
    
    return answer