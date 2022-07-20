# SW Expert Academy 
# 4837. [파이썬 S/W 문제해결 기본- List2] 2일차 - 부분집합의 합 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg

T = int(input())
A = [i for i in range(1, 13)]

for test_case in range(1, T+1 ):
    N, K = map(int, input().split())
    
    m = len(A)
    cnt = 0
    
    for i in range(1 << m):  # 1 << len(A): 부분 집합의 개수
        list = []
        for j in range(m):   # 원소의 수만큼 비트를 비교함
            if (i&(1<<j)):   # i의 j번째 비트가 1이면 j번째 원소 출력
                list.append(A[j])
                
        if len(list) == N and sum(list) == K: # 부분집합 원소의 수가 N이고 부분 집합의 합이 K이면
            cnt += 1
            
    print("#"+str(test_case), cnt)           