import sys
n = int(sys.stdin.readline().strip())
num = list(map(int,sys.stdin.readline().strip().split()))
# 두 수의 공약수 = 최대공약수의 약수
# 유클리드 호제법
# r = x % y
# x,y의 최대 공약수는 y,r의 최대공약수와 같다는 원리
# x값에는 y값을 대입하고, y값에는 r값을 대입하다보면
# 언젠가 r==0이 되는데 이때 y에 있는 값이 최대공약수이다.
def gcd(a,b):
    if b == 0: return a
    return gcd(b,a%b) 
g = gcd(num[0],gcd(num[1],num[-1]))
for i in range(1,g//2+1):
    if g % i == 0:
        print(i) # 최대공약수의 반만큼 검사하여 약수를 구해주어 출력
print(g) # 마지막으로 자기 자신까지 출력해준다.