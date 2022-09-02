import sys
sys.setrecursionlimit(10 ** 6) 
sys.stdin = open("sample_input.txt", "r")
input = sys.stdin.readline

num_list = []

while True:
    try:
        value = int(input())
        num_list.append(value)
    except:
        break

def postorder(s,e):
    if s > e:
        return
    m = e + 1
    for i in range(s+1,e+1):
        # 루트 보다 크면 오른쪽 서브 트리
        if num_list[s] < num_list[i]:
            m = i
            break
    
    postorder(s+1,m-1) # 왼쪽 서브 트리 재귀적으로 탐색
    postorder(m,e) # 오른쪽 서브 트리 재귀적으로 탐색
    print(num_list[s])

postorder(0,len(num_list)-1)