change = int(input())
coin = [5,3]
memo = [0] * (change+1)
result = 0
# 1kg에 대한 최적해 -> (선택)2kg에 대한 최적해 -> (선택)3kg에 대한 최적해
def dp(change):
    global result
    for n in range(1, change+1):
        min = 9999
        for i in range(len(coin)):
            if n >= coin[i]:
                ret = memo[n-coin[i]]
                if min > ret: min = ret
            memo[n] = min + 1
    result = memo[change]
dp(change)    
if result == 10000: print(-1)
else: print(result)