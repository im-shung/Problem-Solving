# SW Expert Academy 
# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVGOEKqeoDFAWg

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    #배열 입력 받기
    arr = []
    for i in range(N):
        arr.append(input()) # arr = ['WPMACSIBIK', 'STWASDCOBQ', 'AMOUENCSOG', 'XTIIGBLRCZ', 'WXVSWXYYVU', 'CJVAHRZZEM', 'NDIEBIIMTX', 'UOOGPQCBIW', 'OWWATKUEUY', 'FTMERSSANL']

    # 가로 검색
    for r in range(N): 
        for c in range(N - M + 1):
            # 회문이 맞는지 확인
            if arr[r][c : c + M] == arr[r][c : c + M][ : : -1]: # [start : end : step] step만큼 문자를 건너뛰면서, start오프셋부터 end-1 오프셋(인덱스)까지 추출
                print(f"#{test_case} {''.join(arr[r][c : c + M])}")
    
    # 세로 검색
    for r in range(N - M + 1):
        for c in range(N):
            arr2 = [] # 세로 열 리스트 만들기
            for i in range(M):
                arr2.append(arr[r+i][c])
            if arr2 == arr2[ : : -1]: # [start : end : step] step만큼 문자를 건너뛰면서, start오프셋부터 end-1 오프셋(인덱스)까지 추출
                print(f"#{test_case} {''.join(arr2)}")