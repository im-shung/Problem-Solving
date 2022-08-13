import sys
input = sys.stdin.readline

n,k,q,m = map(int,input().split())
sleep = set(map(int,input().split())) # set()
students = set(map(int,input().split())) # set()
attend = [False] * (n+3)

# 1. 출석 체크
for s in students-sleep:
    for i in range(s,n+3,s):
        if i not in sleep:
            attend[i] = True 
            
# 2. 미출석자 누적합 구하기
memo = [0 for _ in range(n+3)]
for i in range(3,n+3):
    if not attend[i]: 
        memo[i] = memo[i-1] + 1
    else:
        memo[i] = memo[i-1]
        
# 3. 출력
for _ in range(m):
    s, e = map(int,input().split()) 
    result = memo[e] - memo[s-1]
    print(result)