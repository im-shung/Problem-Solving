n, k = map(int,input().split())
S = [n for n in range(1,int(n)+1)]
answer = []
idx = 0
for i in range(n):
    idx += k-1
    if idx >= len(S): idx %= len(S)
    answer.append(str(S.pop(idx)))
print("<",", ".join(answer)[:],">", sep='')