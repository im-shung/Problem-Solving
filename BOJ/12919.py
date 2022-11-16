import sys
sys.stdin = open("C:\Program_study\AlgorithmStudy\sample_input.txt", "r")

def dfs(a):
    if a == s:
        return 1

    if len(a) == 0: return 0

    if a[-1] == "A":
        dfs(a[:-1])
    if a[0] == "B":
        dfs(a[1:][::-1])

if __name__ == '__main__':
    s = list(input())
    t = list(input())

    print(dfs(t))