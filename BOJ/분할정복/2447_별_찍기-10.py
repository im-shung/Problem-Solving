import sys
input = sys.stdin.readline

n = int(input())

def drawing(n):
    if n == 3:
        return ['***','* *','***']
    arr = drawing(n//3)
    stars = []
    
    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(n//3)+i)
    for i in arr:
        stars.append(i*3)
    return stars    
            
print('\n'.join(drawing(n)))