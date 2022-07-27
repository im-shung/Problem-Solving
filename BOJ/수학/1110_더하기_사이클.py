import sys
x = int(sys.stdin.readline().strip())
cnt = 0
def calc(temp):
    global cnt,x
    cnt += 1
    if temp == x: return
    elif temp >= 10: sum = temp//10+temp%10
    else: sum = temp
    _temp = (temp%10)*10 + sum%10   
    calc(_temp)
if x >= 10: sum = x//10+ x%10
else: sum = x
calc((x%10)*10 + sum%10)
print(cnt)