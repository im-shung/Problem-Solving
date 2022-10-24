n = int(input())

def get_cnt(s):
    m = 0
    for ss in list(str(s)):
        if int(ss) in [3, 6, 9]:
            m += 1
    return m

for i in range(1, n + 1):
    cnt = get_cnt(i)
    if cnt == 0:
        tmp = i
    else:
        tmp = get_cnt(i) * '-'
    if i == n:
        print(tmp)
    else:
        print(tmp, end = " ")
