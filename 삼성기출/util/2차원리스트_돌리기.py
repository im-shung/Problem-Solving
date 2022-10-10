arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]
       ,[16,17,18,19,20],
       [21,22,23,24,25]]

def print_arr():
    for i in arr:
        print(i) 

print("----------------------------------")
print("기존 리스트")
print_arr() 

def rotated(arr):
    print("----------------------------------")
    print("for문 사용해 시계 방향으로 90도 돌리기")
    n = len(arr)
    m = len(arr[0])
    
    result = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = arr[i][j]    
            
    arr = result
    print_arr() 
    

def rotate_clock(arr):
    print("----------------------------------")
    print("zip 사용해 시계 방향으로 90도 돌리기")
    arr = list(map(list, zip(*arr[::-1])))
    print_arr() 
        
def rotate_clock_convert(arr):        
    print("----------------------------------")
    print("zip 사용해 반시계 방향으로 90도 돌리기")
    arr = list(map(list, zip(*arr)))[::-1]
    print_arr() 
        
def rotate_mid_clock_convert(arr):
    print("----------------------------------")
    print("가운데 십자가 모양만 반시계 방향으로 90도 돌리기")
    tmp_arr = list(map(list, zip(*arr)))[::-1]
    
    n = len(arr)
    tmp_r = []
    tmp_c = []
    for i in range(n):
        tmp_r.append(tmp_arr[i][n//2])
    for i in range(n):
        tmp_c = tmp_arr[n//2]
        
    arr[n//2] = tmp_c
    for i in range(n):
        arr[i][n//2] = tmp_r[i]
    print_arr() 


def rote_clock_etc(arr):
    print("----------------------------------")
    print("가운데 십자가 이외 부분 90도 돌리기")
    n = len(arr)
    m = n//2 
    
    def rotate_etc(i, j, ni, nj, m):
        tmp = [[] for _ in range(m)]
        tmp[0] = arr[i][j: nj + 1]
        for x in range(i + 1, ni + 1):
            tmp[x - i] = arr[x][j: nj + 1]
        
        tmp = list(map(list, zip(*tmp[::-1])))
        k = 0
        for x in range(i, ni + 1):
            arr[x][j: nj + 1] = tmp[k]
            k += 1
    
    # 이외 부분 시계방향 90도 돌리기
    rotate_etc(0, 0, m - 1, m - 1, m)
    rotate_etc(0, m + 1, m - 1, n - 1, m)
    rotate_etc(m + 1, 0, n - 1, m - 1, m)
    rotate_etc(m + 1, m + 1, n - 1, n - 1, m)
    
    print_arr() 

rotate_clock(arr)
rotate_clock_convert(arr)
rotate_mid_clock_convert(arr)
rote_clock_etc(arr)
