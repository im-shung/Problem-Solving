# SW Expert Academy 
# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVHzyqqe8DFAWg&&

import sys
sys.stdin = open("../sample_input.txt", "r")

T = int(input())

### DFS + 가지치기 ###
def checkNode(r):
    global sub_result, result
    
    # 조건: 각 row에서 하나씩 숫자를 골라 합이 최소가 되도록 한다.
    # 가지치기
    if result < sub_result:
        return
    
    if r == N: # 마지막 row
        if sub_result < result:
            result = sub_result
    
    for c in range(N): # col 만큼 반복
        if use_check[c]: # True: 해당 row 방문 가능
            use_check[c] = False # 갔던 row는 사용불가하게 바꾸기
            sub_result += arr[r][c]
            
            checkNode(r+1) 
            # 가지치기 당하고 돌아오면
            use_check[c] = True
            sub_result -= arr[r][c]
        
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    use_check = [True for _ in range(N)] 
    sub_result, result = 0, 987654321
    checkNode(0)
    print(f"#{test_case} {result}")
