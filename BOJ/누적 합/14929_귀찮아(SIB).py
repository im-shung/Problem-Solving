# 참고: https://ssafy-story.tistory.com/73

n = int(input())
A = list(map(int,input().split()))
B = []
B.append(A[0])
for i in range(1,n):
    B.append(B[i-1]+A[i])
result = 0
for i in range(n):
    result += A[i] * (B[n-1]-B[i])
print(result)