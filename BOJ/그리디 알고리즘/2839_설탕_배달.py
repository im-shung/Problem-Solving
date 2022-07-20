# 백준
# 2839. 설탕 배달

N = int(input()) 
SUM = 0

i = 0
while N >= 0:
    if N % 5 == 0:
        SUM = i + N// 5
        break
    N -= 3
    i += 1
else: 
    SUM = -1
print(SUM)