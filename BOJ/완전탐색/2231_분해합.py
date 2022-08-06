import sys
n = int(input())
temp = n-1
answer = []
while temp > 0:
    result = temp
    _temp = temp
    while _temp > 0:
        result += _temp%10
        _temp //= 10
    if result == n:
        answer.append(temp)
    temp -= 1
if len(answer) == 0: print(0)
else: print(min(answer))