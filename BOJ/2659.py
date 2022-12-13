def get_sum(a, b, c, d):
    return 1000 * a + 100 * b + 10 * c + d

def get_min(a, b, c, d):
    A = get_sum(a, b, c, d)
    B = get_sum(b, c, d, a)
    C = get_sum(c, d, a, b)
    D = get_sum(d, a, b, c)
    return min(A, B, C, D)

s = list(map(int, input().split()))
new_s = get_min(s[0], s[1], s[2], s[3])

num = [0] * 10000
for n1 in range(1, 10):
    for n2 in range(1, 10):
        for n3 in range(1, 10):
            for n4 in range(1, 10):
                num[get_min(n1, n2, n3, n4)] = 1

cnt = 0
for i in range(1111, new_s + 1):
    if num[i]:
        cnt +=1
print(cnt)
