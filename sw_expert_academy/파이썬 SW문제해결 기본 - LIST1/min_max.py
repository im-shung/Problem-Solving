# SW Expert Academy 
# 4828. [파이썬 S/W 문제해결 기본 - LIST1] 1일차 - min max D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))

    print("#"+str(test_case),max(arr)-min(arr))
