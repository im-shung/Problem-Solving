# SW Expert Academy 
# 4843. [파이썬 S/W 문제해결 기본- List2] 2일차 - 특별한 정렬 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a = list(map(int,input().split()))
    
    for i in range(0,len(a)-1):
        if (i % 2 == 0):
            max = i
            for j in range (i+1, len(a)):
                if a[max] < a[j]:
                    max = j
            a[i],a[max] = a[max], a[i]
        else:
            min = i
            for j in range (i+1, len(a)):
                if a[min] > a[j]:
                    min = j
            a[i],a[min] = a[min], a[i]
    print("#"+str(test_case)," ".join(map(str, a[:10])))
            