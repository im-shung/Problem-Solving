# SW Expert Academy 
# 5258. [파이썬 S/W 문제해결 최적화] 3일차 - 해피박스 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYNxvq3BIDFAVT
# 이해하기 https://jeonyeohun.tistory.com/86
import sys
sys.stdin = open("../sample_input.txt", "r")

# 집합 A가 n번째 보석을 포함하고 있지 않다면, 
# A는 n번째 보석을 뺀 나머지 n-1개의 보석들 중에서 최적으로 고른 부분집합과 같다.

# 집합 A가 n번째 보석을 포함하고 있다면, 
# A에 속한 보석들의 총 가격은 n-1개의 보석들 중에서 최적으로 고른 가격의 합에다가 보석 n의 가격을 더한 것과 같다. (단, n번째 보석을 넣었을 때 배낭이 수용할 수 있어야한다.)

def happy_box(n,m): # 최대 무게, 물건의 번호
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if items[i][0] > j: # i번째 아이템을 넣을 수 없을 때까지는 
                B[i][j] = B[i - 1][j] # i-1번째 아이템 넣은 상태로 둔다
            else: 
                # i번째 아이템을 넣을 수 있을 때
                # 이미 들어있는 i-1번째에 가방의 가치와 
                # 
                B[i][j] = max(B[i - 1][j - items[i][0]] + items[i][1], B[i - 1][j])
    return B[m][n]

for test_case in range(1, int(input())+1):
    n, m = map(int, input().split()) 
    B = [[0 for _ in range(n+1)] for _ in range(m+1)]
    items = [0]
    for _ in range(m):
        s, p = map(int, input().split())
        items.append((s,p,p/s))
    print(B)
    print(f"#{test_case} {happy_box(n,m)}")