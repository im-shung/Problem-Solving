import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    A = list(map(int,input().split()))
    print(min(A),max(A))