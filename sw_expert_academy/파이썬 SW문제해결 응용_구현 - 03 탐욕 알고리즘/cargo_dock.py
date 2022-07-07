# SW Expert Academy 
# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT
    
import sys
sys.stdin = open("../sample_input.txt", "r")      
      
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    A = list()
    for _ in range(N):
        s, e = map(int, input().split())
        A.append((e,s))
        
    # 종료 시간이 빠른 순서로 활동들 정렬 
    A.sort() 
    
    S = [A[0]] # 첫 번째 활동을 선택하고 해집합에 포함
    j = 0
    for i in range(1,N):
        # 선택된 활동의 종료 시간보다 빠른 시작 시간을 가지는 활동을 모두 제거
        # # 남은 활동들에 대해 앞의 과정을 반복
        if A[i][1] >= A[j][0]: 
            S.append(A[i])
            j = i
   
    print(f"#{test_case} {len(S)}")
    
         
