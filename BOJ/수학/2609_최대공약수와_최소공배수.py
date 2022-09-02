import sys
input = sys.stdin.readline

def gcd(a,b):
    if b == 0: return a
    return gcd(b,a%b)
x, y = map(int,input().split())
print(gcd(x,y),x*y//gcd(x,y)) # 최대공약수,최대공배수
