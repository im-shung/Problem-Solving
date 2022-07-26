import sys
sys.stdin = open("sample_input.txt", "r")
N,M = map(int,sys.stdin.readline().split())
Text = [0] * N
for i in range(N):
    Text[i] = sys.stdin.readline().strip()
cnt = 0
for _ in range(M):
    subText = sys.stdin.readline().strip()
    if subText in Text: cnt += 1
print(cnt)