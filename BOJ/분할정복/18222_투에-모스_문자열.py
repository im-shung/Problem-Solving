# 2의 거듭제곱으로 규칙을 찾아야겠다는 것은 인지했는데 규칙을 발견하지 못함
import math
import sys
input = sys.stdin.readline

n = int(input())

# 첫번째 방법: 투에-모스 수열 법칙
'''
투에-모스 수열은 모든 음이 아닌 정수 n에 대해서 다음 점화식을 만족시키는 수열이다.
t(0) = 0
t(2n) = t(n)
t(2n+1) = 1 - t(n)

def tue_morse(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n % 2:
        return 1 - tue_morse(n//2)
    else:
        return tue_morse(n//2)
print(tue_morse(n-1))
'''

# 두번째 방법: 규칙 찾아서 하기
# 참고: https://castlerain.tistory.com/117
def solution(n, k):
    if n == 1:
        print(k) 
        exit(0)
    num = math.log(n, 2)
    if num-int(num) == 0: # 완벽히 나누어 떨어지는 경우
        if num % 2 == 0:
            print(k)
            exit(0)
        else:
            print((k+1)%2)
            exit(0)
    else:
        num = int(num)
    if num % 2 == 0:
        solution(n-2**num, (k+1)%2)
    else:
        k = (k+1) % 2
        solution(n-2**num, k)
solution(n,0)