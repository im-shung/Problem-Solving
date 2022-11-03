for t in range(1, int(input()) + 1):
    bit_list = list(input())
    stack = []
    for bit in bit_list:
        if stack:
            if bit != stack[-1]:
                stack.append(bit)
        else:
            if bit == '1':
                stack.append(bit)

    print(f'#{t} {len(stack)}')