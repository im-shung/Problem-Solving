import sys
input = sys.stdin.readline

cases = [3,1]
n = int(input())

x = 1
while cases[0]*x <= n:
    x += 1
x -= 1
cnt = x + (n - cases[0]*x)
if cnt % 2 == 0:
    turn = "CY"
else:
    turn = "SK"
print(turn)