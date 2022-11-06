import sys
sys.stdin = open("../sample_input.txt", "r")


def is_include(A, B):
    left_x1, left_y1, right_x1, right_y1 = A
    left_x2, left_y2, right_x2, right_y2 = B

    if left_x2 <= left_x1 <= right_x2 and \
            left_x2 <= right_x1 <= right_y2 and \
            left_y2 <= left_y1 <= right_y2 and \
            left_y2 <= right_y1 <= right_y2:
        return True


def is_overlap(A, B):
    left_x1, left_y1, right_x1, right_y1 = A
    left_x2, left_y2, right_x2, right_y2 = B

    if left_x2 <= left_x1 <= right_x2:
        if left_y2 <= left_y1 <= right_y2:
            return get_sum(left_x1, left_y1, right_x2, right_y2)
        elif left_y2 <= right_y1 <= right_y2:
            return get_sum(left_x1, left_y2, right_x1, right_y2)
    else:
        if left_x2 <= right_x1 <= right_x2:
            if left_y2 <= left_y1 <= right_y2:
                return get_sum(left_x2, left_y1, right_x1, right_y2)
            elif left_y2 <= right_y1 <= right_y2:
                return get_sum(left_x2, left_y2, right_x1, right_y1)

    return False
def get_sum(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)

if __name__ == '__main__':
    arr = []
    sum_arr = []
    for i in range(4):
        x1, y1, x2, y2 = map(int, input().split())
        arr.append((x1, y1, x2, y2))
        sum_arr.append(get_sum(x1, y1, x2, y2))

    result = sum(sum_arr)
    memo = [[]] * 4
    for i in range(4):
        for j in range(4):
            if i == j: continue
            if j in memo[i]: continue
            if is_include(arr[i], arr[j]):
                result -= sum_arr[j]
            else:
                temp = is_overlap(arr[i], arr[j])
                if temp:
                    result -= temp

            memo[i].append(j)

    print(result)