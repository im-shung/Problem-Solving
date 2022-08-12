import sys
input = sys.stdin.readline
# sys.stdin = open("sample_input.txt", "r")

n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
matrix = [[0]* (n+1) for _ in range(n+1)]
    
for i in range(1,n+1):
    for j in range(1,n+1):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] + A[i-1][j-1] - matrix[i-1][j-1]      
for _ in range(m):
    i,j,x,y = map(int,input().split())
    result = matrix[x][y] - matrix[x][j-1] - matrix[i-1][y] + matrix[i-1][j-1]
    print(result)