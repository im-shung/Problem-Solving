import sys
sys.stdin = open("sample_input.txt", "r")

while True:
    string = input()
    if string == "END": break
    print(string[::-1])