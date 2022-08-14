for _ in range(int(input())):
    string = input()
    memo = [0] * 26
    for s in string:
        if s.isalpha():
            memo[ord(s)-ord('a')] += 1
    cnt = max(memo)
    if memo.count(cnt) > 1:
        print("?")
    else:
        idx = memo.index(cnt)
        print(chr(ord('a')+idx))