# SW Expert Academy 
# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDLaK1kMDFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")

T = int(input())

hexa_to_decimal = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F':15}

for test_case in range(1, T+1):
    N, hexa = input().split()
    answer = ''
    
    # 둘어온 16진수만큼 반복
    for i in hexa:
        # hexa to decimal
        if '0' <= i <= '9':
            temp = int(i)
        else:
            temp = hexa_to_decimal[i]     
        # decimal to binary    
        # 16진수는 2진수 4글자이므로 8을 이용함
        num = 8
        for _ in range(4):
            # 비트연산해서 값이 나오면 1
            if temp & num:
                answer += '1'
            # 값이 안나오면 0
            else: answer += '0'
            # 비트연산하는 값 나누기 2 하기 
            num >>= 1
    print(f"#{test_case} {answer}")
  