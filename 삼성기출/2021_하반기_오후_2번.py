n, k = map(int,input().split())
arr = list(map(int,input().split()))

def rotated(A):
    n = len(A)
    m = len(A[0])
    
    result = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = A[i][j]    
    return result

def plus():
    global arr

    mn = min(arr)
    index = list(filter(lambda x: arr[x] == mn, range(len(arr))))
    for i in index:
        arr[i] += 1


def roll():
    global arr

    # 초기화
    tmp = [ [arr[0]], arr[1:] ]
    while True:
        tmp2 = tmp[:-1] # 밑단 도우를 제외한 나머지
        t = len(tmp2[0])
        slice = tmp[-1][:t] # 밑단 도우에서 떼어낸 조각
        rest = tmp[-1][t:] # 밑단 도우에서 떼어낸 조각 외의 나머지 부분
        
        # 새로 붙이기
        tmp2.append(slice)  
        tmp = list(map(list,zip(*tmp2[::-1]))) + [rest]
        if len(tmp[-2]) <= len(tmp[-1]):
           arr = tmp
        else:
            break 

def press():
    global arr
    
    memo = []
    visited = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            visited.append((i, j))
            for _x, _y in [(1,0), (-1,0), (0,1), (0,-1)]:
                dx, dy = i + _x, j + _y
                if not (0 <= dx < len(arr) and 0 <= dy < len(arr[dx])): 
                    continue
                if (dx, dy) in visited:
                    continue
                
                mx = max( arr[i][j], arr[dx][dy] ) 
                mn = min( arr[i][j], arr[dx][dy] )    
                d = (mx - mn) // 5
                if mx == arr[i][j]:
                    memo.append((i, j, -d))
                    memo.append((dx, dy, d))
                else:
                    memo.append((i, j, d))
                    memo.append((dx, dy, -d))
                    
    for x, y, val in memo:
        arr[x][y] += val
        
    tmp = []
    for i in range(len(arr[-1])):
        for j in range(len(arr) - 1, -1, -1):
            if len(arr[j]) <= i:
                continue
            tmp.append(arr[j][i])
    arr = tmp
    

def fold():
    global arr
    
    n = len(arr) // 2
    tmp = [ arr[:n][::-1] , arr[n:] ]
    
    s1 = []
    s2 = []
    m = n // 2
    for i in range(len(tmp)):
        s1.append(tmp[i][:m])
        s2.append(tmp[i][m:])
    s1 = rotated(s1); s1 = rotated(s1)
    
    arr = []
    for s in s1:
        arr.append(s)
    for s in s2:
        arr.append(s)

def pro():
    cnt = 0
    while True:
        cnt += 1
        # 1. 밀가루 양이 가장 작은 위치에 밀가루 1만큼 더 넣어줍니다.(가장 작은 위치가 여러 개라면 모두 넣기)
        plus()
        # 2. 도우를 말아줍니다.
        roll()
        # 3. 도우를 꾹 눌러줍니다.
        press()
        # 4. 도우를 두 번 반으로 접어줍니다.
        fold()
        # 3의 과정만 한번 더 진행합니다.
        press()

        mx = max(arr)
        mn = min(arr)
        if mx - mn <= k:
            break
    print(cnt)
pro()