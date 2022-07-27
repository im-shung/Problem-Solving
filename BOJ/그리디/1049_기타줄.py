# 백준
# 1049. 기타줄

N, M = map(int, input().split())
PACKAGE = 1001; ITEM = 1001;

for test_case in range(0,M):
    x, y = map(int, input().split())
    
    if PACKAGE > x:
        PACKAGE = x
    if ITEM > y:
        ITEM = y

SUM = 0
# 패키지 가격이 날개 가격 x 6보다 클 때
if PACKAGE > ITEM * 6:
    SUM = ITEM * N
else:
    # 패키지 가격이 더 저렴할 때
    # N을 6으로 나눈 몫 만큼 패키지로 구매한다. 
    SUM += PACKAGE * (N//6)
    
    # 남은 날개의 가격이 패키지보다 크면 패키지를 구매한다.
    # 아니면 날개로 구매한다.
    if ITEM * (N%6) > PACKAGE:
        SUM += PACKAGE
    else:
        SUM += ITEM * (N%6) 
print(SUM)
