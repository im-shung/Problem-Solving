# SW Expert Academy 
# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVGOEKqeoDFAWg

### 보이어-무어 알고리즘 이용 버전 ###

T = int(input())

for test_case in range(1, T +1):
    N = list(input())
    M = list(input())
    
    n = len(N)
    m = len(M)
    

    # skip 배열 생성 
    skip = dict()
    for i in range(n):
        skip[N[i]] = n-1-i

    result = 0
    i = n - 1
    cur = n - 1
    while i < m:
        if cur == -1: # N을 뒤에서부터 처음까지 다 비교한 뒤
            result = 1
            break
        if M[i] == N[cur]: 
            # 패턴의 끝 원소와 일치하면
            i -= 1
            cur -= 1
        else:
            # 패턴의 끝 원소와 일치하지 않으면
            if (skip.get(M[i]) != None): # skip 배열에 원소가 있으면 해당 값을 더한다.
                i += int(skip.get(M[i]))
            else: # skip 배열에 원소가 없으면 패턴의 길이만큼 더한다.
                i += n
            cur = n - 1
                   
    print(f"#{test_case} {result}")