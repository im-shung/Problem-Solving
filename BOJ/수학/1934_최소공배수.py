import sys
# input = sys.stdin.readline
sys.stdin = open("sample_input.txt", "r")

# 최대공약수
def gcd(a,b):
    if b == 0: return a
    return gcd(b,a%b)
for _ in range(int(input())):
    x, y = map(int,input().split())
    print(x*y//gcd(x,y)) # 최소공배수
