# SW Expert Academy 
# 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수 D2 
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVGOEKqeoDFAWg

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    str3 = dict()
    
    for i in range(len(str1)):
        str3[str1[i]] = 0
        if str1[i] in str2:
            str3[str1[i]] += str2.count(str1[i])
            
    print(f"#{test_case} {max(str3.values())}")