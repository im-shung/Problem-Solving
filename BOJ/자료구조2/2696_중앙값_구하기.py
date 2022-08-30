import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    num_array = []
    if n > 10:
        for _ in range(n//10+1):
            num_array.extend(list(map(int,input().split())))
    else: num_array.extend(list(map(int,input().split())))
    result = []
    hq = []
    for i in range(n):
        heapq.heappush(hq,num_array[i])
        if i == 0:
            result.append(num_array[i])
        else:
            if i % 2 == 0:
                s = []
                for _ in range(len(hq)//2+1):
                    s.append(heapq.heappop(hq))
                result.append(s[-1])
                for i in s:
                    heapq.heappush(hq,i)
    print(len(result))
    if len(result) > 10:
        for i in range(len(result)):
            print(result[i], end =" ")
            if (i+1) % 10 == 0 :
                print()
    else: print(*result)