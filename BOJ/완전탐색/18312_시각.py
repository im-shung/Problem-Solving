import sys
input = sys.stdin.readline

n,k = map(int,input().split())
cnt = 0
for h in range(n+1):
    for m  in range(60):
        for s in range(60):
            cnt += str(k) in f"{h:02d}{m:02d}{s:02d}" # 0:채워질 문자, 2:총 자리수, d:정수
print(cnt)