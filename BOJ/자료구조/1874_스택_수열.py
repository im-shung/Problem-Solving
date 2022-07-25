import sys
N = int(sys.stdin.readline())
S = [0]; push = [0]; result = []
for i in range(N):
    n = int(sys.stdin.readline());
    if push[-1] > n: # push하는 순서는 오름차순
        if n in S:
            i = len(S)-1
            while S[i] != n:
                S.pop()
                result.append("-")
                i -= 1
        else: 
            result.clear(); result.append("NO"); break
    else:
        for i in range(push[-1]+1,n+1):
            push.append(i)
            S.append(i)
            result.append("+")
    if S[-1] == n:
        S.pop()
        result.append("-")
print("\n".join(result))