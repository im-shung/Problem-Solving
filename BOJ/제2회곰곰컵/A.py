import sys

if __name__ == '__main__':
    n = int(input())
    inputs = sys.stdin.read().replace("D-", "").split()
    print(len(list(filter(lambda x: int(inputs[x]) <= 90, range(n)))))
