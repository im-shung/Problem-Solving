import sys
input = sys.stdin.readline

string1, string2 = input().strip(), input().strip()
l1,l2 = len(string1), len(string2)
memo = [0] * l2
for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < memo[j]:
            cnt = memo[j]
        elif string1[i] == string2[j]:
            memo[j] = cnt + 1
print(max(memo))