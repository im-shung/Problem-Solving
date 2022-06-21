# SW Expert Academy 
# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVGOEKqeoDFAWg


T = int(input())

for test_case in range(1, T +1):
    N = input()
    M = input()
    
    if N in M:
        result = 1
    else:
        result = 0
             
    print(f"#{test_case} {result}")
