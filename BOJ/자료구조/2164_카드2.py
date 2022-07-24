from collections import deque
n = int(input())
D = deque()
for i in range(1,n+1): D.append(i)
while len(D) > 1:
    D.popleft() # 제일 위에 있는 카드 버리기
    D.append(D.popleft()) # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기기
print(D.popleft())