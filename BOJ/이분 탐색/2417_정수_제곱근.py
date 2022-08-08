import sys
input = sys.stdin.readline

n = int(input().strip())
start = 0
end = n
answer = []
while start <= end:
    mid = (start + end) // 2
    if (mid ** 2) > n:
        end = mid -1
    elif (mid ** 2) < n:
        start = mid + 1
    else: 
        answer.append(mid)
        break
if len(answer) == 0:
    print(start)
else: print(*answer)
