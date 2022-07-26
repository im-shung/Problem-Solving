import sys
Dict = {}
names = set()
hq = []
cnt = 0
while True:
    tree_name = sys.stdin.readline().rstrip()
    if not tree_name : break
    try:
        Dict[tree_name] += 1
    except:
        Dict[tree_name] = 1
    cnt += 1
names = [x for x in Dict.keys()]
names.sort()
for name in names:
    ratio = (Dict[name]/cnt) * 100
    # print(name,round(ratio,4)) # round함수는 예상치못한 결과가 발생하기 때문에 안전하지 않다.
    print('%s %.4f'%(name,(Dict[name]/cnt) * 100))  