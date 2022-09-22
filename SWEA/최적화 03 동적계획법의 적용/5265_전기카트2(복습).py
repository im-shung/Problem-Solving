# runtime error
import itertools

for t in range(int(input())):
    n = int(input())
    e = [list(map(int,input().split())) for _ in range(n)]
    cases = list(itertools.permutations(range(1,n)))
   
    min = 1e9
    for case in cases:
        sum = e[0][case[0]] + e[case[-1]][0]
        for i in range(len(case)-1):
            sum += e[case[i]][case[i+1]]
            if sum > min: break
        if sum < min:
            min = sum    
    print(f"#{t+1} {min}")