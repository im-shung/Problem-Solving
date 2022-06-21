### Basic Code ### 

# 정수
# 최소값 출력 

# ans = 99999 # 보통 문제에서 주어지는 입력 범위 값보다 큰 값을 설정
# 또는 
# import sys
# ans = sys.maxsize

for num in map(int,input().split()):
    if ans > num:
        ans = num
print(ans)