import sys
sys.stdin = open("sample_input.txt","r")
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
    print(name,round(ratio,4))