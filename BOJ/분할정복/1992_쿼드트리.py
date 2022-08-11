n = int(input())
A = [list(map(int,input())) for _ in range(n)]
def quad_tree(n,x,y):
    check = A[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != A[i][j]:
                check = -1
                break
            
    if check == -1:
        print("(",end='')
        n //= 2
        quad_tree(n, x, y) # 왼쪽 위
        quad_tree(n, x, y + n) # 오른쪽 위
        quad_tree(n, x + n, y) # 왼쪽 아래
        quad_tree(n, x + n, y + n) # 오른쪽 아래
        print(")",end="")
        
    elif check == 1:
        print(1,end="")
    else:
        print(0,end="")
quad_tree(n,0,0)