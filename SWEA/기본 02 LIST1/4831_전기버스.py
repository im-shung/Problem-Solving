# SW Expert Academy 
# 4831. [파이썬 S/W 문제해결 기본 - LIST1] 1일차 - 전기버스 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg

T = int(input())

for test_case in range(1, T + 1):
    # K : 충전하면 갈 수 있는 정거장 수
    # N : 종점
    # M : 충전기가 위치한 정거장 수
    K, N, M = map(int,input().split())
    # bus : 노선 // 0:충전기X정거장 1:충전기O정거장
    # bus = [0 0 0 0 0 0 0 0 0 0 0] 초기화
    bus = [0 for _ in range(N+1)]
    # arr : 충전기가 위치한 정거장 노드 [1 3 5 7 9]
    arr = list(map(int, input().split()))
    # 충전기가 있는 정거장은 1로 // bus = [0 1 0 1 0 1 0 1 0 1 0]
    for i in arr:
        bus[i] = 1
        
    # 3번째 정거장에서 충전, 6번째에는 충전기가 없으니까 5번째에서 충전, 8번째 없으니까 7번째에서 충전 >> 10번째 도달 (종료)
    # 1. 현재 정거장에서 (현재 + K)번째 정거장까지 갈 수 있음
    # 2. (현재 + K)번째 정거장에 충전기가 없으면 노드를 하나씩 줄여가며 충전기가 있는 정거장을 찾아 충전
    # 3. 충전하면, 현재 버스 위치를 충전한 정류장 인덱스로 갱신 & 충전횟수 1 증가
    # 4. (현재 + K)번째 정거장이 종점 이상이면 종료
    
    # now : 현재 위치
    now = 0; 
    nowK = 0 + K
    cnt = 0
    
    while nowK < N:
        # 현재위치부터 (현재+K)번째 사이에 충전기가 있는 정거장이 없으면 0
        if now == nowK:
            cnt = 0
            break
        # nowK 번째 정거장에 충전기가 있는 경우
        if bus[nowK] == 1:
            now = nowK
            nowK = now + K
            cnt += 1
        # nowK 번째 정거장에 충전기가 없는 경우
        elif bus[nowK] == 0:
            nowK -= 1
    print("#"+str(test_case),cnt)        
            
