# SW Expert Academy 
# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDLaK1kMDFAVT

import sys
sys.stdin = open("../sample_input.txt", "r")

T = int(input())


for test_case in range(1, T+1):
    N = float(input())
    answer = ''
    
    num = 0.5
    i = 1
    while i <= 12:
        if N >= num:
            answer += '1'
            N -= num
            if N == 0: 
                print(f"#{test_case} {answer}")
                break
        else: answer += '0'
        num /= 2
        i += 1
        
    if i == 13:
        print(f"#{test_case} overflow")

   
    
  