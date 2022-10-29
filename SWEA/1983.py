import math

score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    stu = []
    for idx in range(1, n + 1):
        a, b, c = map(int, input().split())
        result = a * 0.35 + b * 0.45 + c * 0.2
        stu.append([result, idx])
    stu.sort(key = lambda x: -x[0])
    stu_idx = list(filter(lambda x: stu[x][1] == k, range(n)))[0] + 1

    print(f'#{t} {score[math.ceil(stu_idx/(n//10)) - 1]} ')