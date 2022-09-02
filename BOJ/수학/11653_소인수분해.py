from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
if n != 1:
    q,r = 0,n
    while True:
        for x in range(2,r+1):
            if r % x == 0:
                q,r = x,r//x
                print(q)
                break
        if r == 1: break