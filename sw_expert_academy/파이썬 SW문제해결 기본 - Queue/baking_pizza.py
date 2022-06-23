# SW Expert Academy 
# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg

import sys
sys.stdin = open("../sample_input.txt", "r")


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int,input().split()) # N: 큐의 크기, M: 원소 개수 
    cheeses = list(map(int,input().split())) # 원소의 값 C
    
    fire_pit = list(range(N)) # 화덕에 피자 미리 넣어놓기

    while len(fire_pit):
        # 가장 먼저 들어온 피자를 검사
        check = fire_pit.pop(0)
        # 치즈를 반으로 나눈 뒤 결과 검사
        cheeses[check] = cheeses[check]//2
        # 치즈가 다 녹은 경우
        if cheeses[check] == 0:
            # 더 넣을 피자 가 있는지 검사
            if N < M:
                # 있으면 새로운 피자를 넣음
                fire_pit.append(N)
                # 다음에 넣을 피자 번호 생성
                N += 1
        else:
            # !!! 치즈가 다 녹지 않은 경우 다시 넣음 !!!
            fire_pit.append(check)
    print(f"#{test_case} {check+1}")
    
        