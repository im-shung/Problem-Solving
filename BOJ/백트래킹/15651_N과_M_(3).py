import itertools
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
for i in itertools.product(range(1,n+1),repeat = m):
    print(*i)