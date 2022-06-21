# SW Expert Academy 
# 4836. [파이썬 S/W 문제해결 기본 - List2] 2일차 - 색칠하기 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg

T = int(input())

for test_case in range(1, T + 1):
    # 칠할 영역 개수
    N = int(input())
    
    # 색 1,2 의 위치를 저장
    colors = [set(), set()]  # set은 중복 허용 x, 순서가 없음(Unordered)
    
    # 영역 개수 만큼 반복
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
    
        # (x1,y1) 부터 (x2, y2)까지 colors에 따라 담는다.
        for x in range(x1, (x2+1)):
            for y in range(y1, (y2+1)):
                colors[color-1].add((x,y))
                
    # 겹치는 부분만 꺼낸다
    # set 자료형의 교집합 활용
    result = colors[0] & colors[1]
    print("#"+str(test_case),len(result))    