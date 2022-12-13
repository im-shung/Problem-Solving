s = input()
ans = []
if "::" in s:
    tmp = s.split("::")

    front, back = [tmp[0]], [tmp[1]]

    if ":" in tmp[0]:
        front = tmp[0].split(":")
    if ":" in tmp[1]:
        back = tmp[1].split(":")

    f_len = len(front)
    b_len = len(back)

    for _ in range(f_len + b_len, 8):
        front.append('0000')
    ans = front + back

else:
    S = s.split(":")
    for i in range(8):
        ans.append(S[i])

answer = ''
for i in range(8):
    tmp = (4 - len(ans[i])) * '0'
    answer += tmp + ans[i] + ":"
print(answer[:-1])