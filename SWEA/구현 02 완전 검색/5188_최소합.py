# SW Expert Academy 
# 5188. [파이썬 S/W 문제해결 구현 - 완전 검색] 2일차 - 최소합 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT
      
import sys
sys.stdin = open("../sample_input.txt", "r")      
      
T = int(input())

direction = [(1,0),(0,1)]

def combination(c,r,sum): # 행,열
    global min
    
    if c >= N or r >= N:
        return
    
    sum += arr[c][r]
    
    if c == N-1 and r == N-1:
        if min > sum:
            min = sum
        return
    elif sum > min:
        return

    for dc, dr in direction:
        nc = dc + c
        nr = dr + r
        if nc < N and nr < N:
            combination(nc,nr,sum)

for test_case in range(1, T+1):
    N = int(input()) # 가로 세로 칸 수 N
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    min = 987654321
    combination(0,0,0) 
    print(f"#{test_case} {min}")
            
            
        
    