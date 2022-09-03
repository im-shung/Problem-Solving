import sys
input = sys.stdin.readline

n = int(input())
drink = list(map(int,input().strip().split()))
drink.sort()
while len(drink) > 1:
    min = drink.pop(0)
    max = drink.pop(len(drink)-1)
    drink.append(max+min/2)
print(*drink)    