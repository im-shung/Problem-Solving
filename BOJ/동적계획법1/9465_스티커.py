import sys
# input = sys.stdin.readline
sys.stdin = open("sample_input.txt", "r")

for t in range(int(input())):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(2)]
    for i in range(1, n):
        if i == 1:
            s[0][i] += s[1][i - 1]
            s[1][i] += s[0][i - 1]
        else:
            s[0][i] += max(s[1][i - 1], s[1][i - 2])
            s[1][i] += max(s[0][i - 1], s[0][i - 2])     
    print(max(s[0][n - 1], s[1][n - 1]))

# 생각은 했는데 구현을 못하겠음
# for t in range(int(input())):
#     n = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(2)]
#     dp = [ [0 for _ in range(n + 1)] for _ in range(2)]
#     for i in range(n - 2):
#         if dp[1][i] == 0:
#             if matrix[1][i + 1] + matrix[0][i + 2] > matrix[1][i + 2]:
#                 dp[1][i + 1] = dp[0][i + 2] = matrix[1][i + 1] + matrix[0][i + 2]
#             else:
#                 dp[1][i + 2] = matrix[1][i + 2]
#         if dp[0][i] == 0:
#             if matrix[0][i + 1] + matrix[1][i + 2] > matrix[0][i + 2]:
#                 dp[0][i + 1] = dp[1][i + 2] = matrix[0][i + 1] + matrix[1][i + 2]
#             else:
#                 dp[0][i + 2] = matrix[0][i + 2]
#     print(dp[-1])
       