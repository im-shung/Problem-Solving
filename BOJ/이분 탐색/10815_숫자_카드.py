import sys
input = sys.stdin.readline
def binary(a,t,start,end):
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == t:
            return mid
        elif a[mid] > t:
            end = mid - 1
        else: 
            start = mid + 1
    return None
n = int(input().strip())
card = list(map(int,input().strip().split()))
m = int(input().strip())
check = list(map(int,input().strip().split()))
card.sort()
for i in range(m):
    if binary(card,check[i],0,n-1) != None:
        print(1, end=" ")
    else:
        print(0, end=" ")