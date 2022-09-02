from collections import defaultdict
import sys
sys.stdin = open("sample_input.txt", "r")
# input = sys.stdin.readline

n = int(input())
graph = defaultdict(int)
for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u] += 1
    graph[v] += 1
for _ in range(int(input())):
    t,k = map(int,input().strip().split())
    if t==1 and graph[k] == 1: print("no")
    else: print("yes")