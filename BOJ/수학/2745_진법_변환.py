import sys
s, n = sys.stdin.readline().strip().split()
j = 10
to = {}
answer = 0
for i in range(ord('A'),ord('Z')+1):
    to[chr(i)] = j
    j+=1
for i in range(len(s)):
    if '0' <= s[i] <= '9': temp = int(s[i])
    else: temp = to[s[i]]
    for j in range(len(s)-i-1):
        temp *= int(n)
    answer += temp
print(answer)