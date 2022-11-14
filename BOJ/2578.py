import sys
sys.stdin = open("C:\Program_study\AlgorithmStudy\sample_input.txt", "r")

from _collections import defaultdict

diag = [(0 ,0), (1, 1), (2, 2), (3, 3), (4, 4)]
diag_r = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]

def horizontal(r):
    if sum(matrix[r]) == 0: return True
    return False

def vertical(c):
    tmp = 0
    for i in range(5):
        tmp += matrix[i][c]
    if tmp == 0: return True
    return False

def diagonal(arr):
    tmp = 0
    for r, c in arr:
        tmp += matrix[r][c]
    if tmp == 0: return True
    return False

def printf(arr):
    for aa in arr:
        for a in aa:
            print(f'{a:2}', end=" ")
        print()
    print()

def sol():
    result = 0
    vertical_visit = []
    horizontal_visit = []
    diagonal_visit = False
    diagonal_r_visit = False
    for cnt, num in enumerate(answer):
        r, c = idx_dict[num]
        matrix[r][c] = 0

        # printf(matrix)

        if (not c in vertical_visit) and vertical(c):
            vertical_visit.append(c)
            result += 1

        if (not r in horizontal_visit) and horizontal(r):
            horizontal_visit.append(c)
            result += 1

        if (not diagonal_visit) and diagonal(diag):
            diagonal_visit = True
            result += 1

        if (not diagonal_r_visit) and diagonal(diag_r):
            diagonal_r_visit = True
            result += 1

        if result >= 3:
            return cnt + 1


if __name__ == '__main__':
    matrix = []
    idx_dict = defaultdict(tuple)
    for _ in range(5):
        matrix.append(list(map(int, input().split())))

    for r in range(5):
        for c in range(5):
            idx_dict[matrix[r][c]] = (r,c)

    answer = []
    for _ in range(5):
        answer.extend(list(map(int, input().split())))

    print(sol())