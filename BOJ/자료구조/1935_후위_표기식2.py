import sys
input = sys.stdin.readline

n = int(input().strip())
ex = list(input().strip())
dict = {}
stack = []
for word in ex:
    if word.isalpha():
        if dict.get(word) == None:
            dict[word] = input().strip()
        stack.append(dict[word])
    else:
        a = str(stack.pop())
        b = str(stack.pop())
        stack.append(eval(str(b+word+a)))
print("{:.2f}".format(*stack))