# 백준
# 1026. 보물

N = int(input()) 
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 오름차순 정렬
A.sort()

# sortB는 B의 내림차순 정렬
sortB = B.copy()
sortB.sort()
sortB.reverse()

SUM = 0     
for i in range(0,N):
    # A의 요소 x B의 요소가 최솟값을 갖게 하려면
    # B의 k번째로 큰 요소 X A의 K번째 작은 요소 
    index = B.index(sortB[i])
    SUM += A[i] * B[index]

print(SUM)

    