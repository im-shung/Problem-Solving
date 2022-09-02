import sys
input = sys.stdin.readline

# 최대공약수
def gcd(a,b):
    if b == 0: return a
    return gcd(b,a%b)
# 최소공배수
def get(a,b):
    max_num,min_num = max(a,b),min(a,b)
    key = min_num
    cnt = 1
    while True:
        if key % max_num == 0:
            return key
        else:
            cnt += 1
            key = min_num * cnt
x, y = map(int,input().split())
print(gcd(x,y),get(x,y))
