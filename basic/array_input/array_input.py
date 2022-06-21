### Basic Code ### 

# 배열 입력

# 첫 번째 줄에는 입력되는 숫자들의 줄 수가 주어지며,
# 다음 줄 부터 숫자들이 공백을 기준으로 주어집니다.

# 예시
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# Good Code
MAP = [list(map(int,input().split())) for _ in range(int(input()))]

#Bad Code
for i in range(int(input())): 
    inputStr = input() 
    arr = list(inputStr) 
    MAP.append(arr)