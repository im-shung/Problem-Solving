from collections import Counter

def win(A, B, x):

    if A.get(x) is None:
        A[x] = 0
    if B.get(x) is None:
        B[x] = 0

    if A.get(x) > B.get(x):
        return "A"
    elif A.get(x) < B.get(x):
        return "B"
    return "D"

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))

        a_dict = Counter(A[1:])
        b_dict = Counter(B[1:])

        result = ''
        for i in range(4, 0, -1):
            result = win(a_dict, b_dict, i)
            if result != "D":
                break
        print(result)


