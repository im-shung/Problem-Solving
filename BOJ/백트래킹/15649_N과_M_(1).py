import itertools
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
for i in itertools.permutations(range(1,n+1),m):
    print(*i)