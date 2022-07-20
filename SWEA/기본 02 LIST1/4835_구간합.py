# SW Expert Academy 
# 4835. [파이썬 S/W 문제해결 기본 - LIST1] 1일차 - 구간합 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # N개의 정수 배열에서 이웃한 M개의 합 중 최대값-최소값 구하는 문제
    # M 개씩 묶어서 합을 구해서 비교
    # 0부터 M 까지 1+2+3
    # 1부터 M+1 까지 2+3+4 ...
    # N-M 부터 N 까지 하면 종료
    
    sum = 0
    min = 987654321
    max = 0 

    # 전에 더한 값보다 
    # 작으면 min에 대입
    # 크면   max에 대입
    index = 0
    while index + M <= N:
        for i in range(M):
            sum += arr[index + i]
        if sum < min:
            min = sum
        if sum > max:
            max = sum
        index += 1
        sum = 0
    print("#"+str(test_case), max - min)

    