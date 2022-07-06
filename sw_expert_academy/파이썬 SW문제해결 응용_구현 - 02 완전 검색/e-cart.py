# SW Expert Academy 
# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT
      
import sys
sys.stdin = open("../sample_input.txt", "r")      
      
import itertools      
      
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)] # e[출발][도착]: 출발지에서 도착지까지 배터리 사용량
    mylist = [i for i in range(1,N)]
    result = list(itertools.permutations(mylist)) # 중복 없는 순열 생성
    
    min = 987654321
    n = len(result)
    m = len(result[0])
    
    for i in range(0,n):
        sum = e[0][result[i][0]] + e[result[i][-1]][0] # 사무실에서 출발, 도착하는 배터리 사용량 더하기
        for j in range(0, m-1):
            start = result[i][j]
            end = result[i][j+1]
            sum += e[start][end]
        if sum < min:
            min = sum
    print(f"#{test_case} {min}")
            
            
    
