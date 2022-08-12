# i=1, j=2, x=2, y=3이라고 했을 때
#(1,2), (1,3), (2,1), (2,2), (2,3)의 합을 구하는 게 아니라 
# (1, 2), (1, 3), (2,2), (2,3)의 합을 구해야 된다.

n,m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]

for _ in range(int(input())):
    i,j,x,y = map(int,input().split())
    i -= 1; j -=1; x -= 1; y -=1;
    result = 0
    if j == y and i == x:
        result = A[i][j]
    elif j == y:
        for row in A[i:x+1]:
            result += row[j]
    elif i == x:
        result = sum(A[x][j:y+1])
    else:
        for row in A[i:x+1]:
            result += sum(row[j:y+1])
    print(result)