def sol(A):
    global result

    if len(A) == 0:
        return

    if A == S:
        result = 1
        return

    if A[-1] == 'A':
        sol(A[:-1])

    tmp = A[::][::-1]
    if tmp[-1] == 'B':
        sol(tmp[:-1])

S = input()
T = input()

result = 0
sol(T)
print(result)
