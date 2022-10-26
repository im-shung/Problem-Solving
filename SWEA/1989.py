import sys
sys.stdin = open("../sample_input.txt", "r")

for t in range(1, int(input()) + 1):
    s = list(input().strip())
    result = 0
    if s[::] == s[::][::-1]:
        result = 1
    print(f'#{t} {result}')