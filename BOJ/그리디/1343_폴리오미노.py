n = list(input())
answer = []
answer.extend(n)
cnt = 0
for i in range(len(n)):
    if n[i] == 'X': 
        cnt += 1
    else:
        cnt = 0
    if cnt == 2:
        for i in range(i-1,i+1):
            answer[i] = 'B'
    if cnt == 4: 
        for i in range(i-3,i+1):
            answer[i] = 'A'
        cnt = 0
if 'X' in answer:
    print(-1)
else: print(''.join(map(str,answer)))