# SW Expert Academy 
# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT
    
import sys
sys.stdin = open("../sample_input.txt", "r")      
      
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split()) # 컨테이너 수 N, 트럭 수 M
    w_arr = list(map(int, input().split())) # 화물 무게 리스트
    t_arr = list(map(int, input().split())) # 트럭 적재용량 리스트
    
    # 내림차순 정렬
    w_arr.sort(); w_arr.reverse()
    t_arr.sort(); t_arr.reverse()
    
    w_selected = [0] * N # 컨테이너 이용 가능 여부 저장
    t_selected = [0] * M # 트럭 이용 가능 여부 저장
    
    sum = 0
    for i in range(M): 
        if t_selected[i] == 0: # i번째 트럭 이용 가능 하다면
            for j in range(N): 
                if w_selected[j] == 0: # j번째 컨테이너 이용 하다면
                    if t_arr[i] >= w_arr[j]:
                        sum += w_arr[j] 
                        t_selected[i] = 1
                        w_selected[j] = 1
                        break
    print(f"#{test_case} {sum}")
    
         
