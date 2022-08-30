from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

max_heap,min_heap = [], []
in_list = defaultdict(bool)
for _ in range(int(input())):
    p, l = map(int,input().split())
    heapq.heappush(min_heap,[l,p]) # [난이도,문제번호]
    heapq.heappush(max_heap,[-l,-p]) # [-난이도,-문제번호]
    in_list[p] = True
for _ in range(int(input())):
    command = input().strip().split()
    if command[0] == "recommend":
        if command[1] == '1':
            while not in_list[-max_heap[0][1]]:
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        else:
            while not in_list[min_heap[0][1]]: # visit이 False일떄 -> 해당노드가 삭제된상태
                heapq.heappop(min_heap) # 이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
            print(min_heap[0][1])
    elif command[0] == "solved":
        in_list[int(command[1])] = False
    else:
        p,l = int(command[1]), int(command[2])
        while not in_list[-max_heap[0][1]]: 
            heapq.heappop(max_heap)
        while not in_list[min_heap[0][1]]: 
            heapq.heappop(min_heap) 
        in_list[p] = True
        heapq.heappush(min_heap,[l,p]) 
        heapq.heappush(max_heap,[-l,-p]) 