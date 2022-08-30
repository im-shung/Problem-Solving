import heapq
import sys
sys.stdin = open("sample_input.txt", "r")

input = sys.stdin.readline

for _ in range(int(input())):
    min_heap,max_heap = [], []
    visited = [False] * 1_000_001
    for i in range(int(input())):
        ex = input().strip().split()
        str,val = ex[0],ex[1]
        if str == 'I':
            heapq.heappush(min_heap,(int(val),i))
            heapq.heappush(max_heap,(-int(val),i))
            visited[i] = True
        elif str == 'D':
            if val == '-1':
                while min_heap and not visited[min_heap[0][1]]: # visit이 False일떄 -> 해당노드가 삭제된상태
                    heapq.heappop(min_heap) # 이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
                if min_heap:
                    visited[min_heap[0][1]] = False # visited이 Ture였으므로 False로 바꾸고 삭제함
                    heapq.heappop(min_heap)
            else:
                while max_heap and not visited[max_heap[0][1]]: 
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            
# 모든 연산이 끝난후에도 쓰레기 노드가 들어있을수 있으므로, 결과를 내기전 모두 비우고 각 힙의 첫번째 원소값을 출력한다. 
    while min_heap and not visited[min_heap[0][1]]: heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]: heapq.heappop(max_heap)
    if min_heap and max_heap:
        print(-(heapq.heappop(max_heap))[0],  heapq.heappop(min_heap)[0])
    else:
        print('EMPTY')