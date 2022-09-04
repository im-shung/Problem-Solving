# n진수로 변환하는 함수
def convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

# 소수인지 판별하는 함수
def is_prime(x):
    if len(x) == 0: return False
    x = int(''.join(map(str,x)))
    if x == 1: return False
    flag = True
    for i in range(2, x + 1):
        if i * i > x: break
        if x % i == 0:
            flag = False
            break
    return flag

def solution(n, k):
    num = list(map(int,convert(n,k)))
    zero_list = list(filter(lambda x: num[x] == 0, range(len(num))))
    answer = 0
    if len(zero_list) == 0:
        if is_prime(num):
            answer += 1
    else:
        if zero_list[0] != 0:
            if is_prime(num[0:zero_list[0]]):
                answer += 1
        if zero_list[-1] != len(num)-1:
            if is_prime(num[zero_list[-1]+1:]):
                answer += 1
        for i in range(len(zero_list)-1):
            if is_prime(num[zero_list[i]+1:zero_list[i+1]]):
                answer += 1
    return answer