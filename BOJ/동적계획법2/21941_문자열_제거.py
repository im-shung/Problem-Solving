from collections import defaultdict
import re
import sys

S = input()
dic = defaultdict()
for _ in range(int(input())):
    A, X = input().split()
    dic[A] = int(X)
list = list(dic.keys())

def dp(A,S):
    score = 0
    if A in S:
        if len(i) < dic[i]:
            score += dic[i]
        else:
            score += len(i)
        S = re.sub(i,"_"*len(i),S,1)
        dp(A,S)
    else:
        for s in S:
            if s != '_':
                score += 1
    return score

max = len(S)
for i in list:
    score = dp(i,S)
    if max < score:
        max = score
print(max)