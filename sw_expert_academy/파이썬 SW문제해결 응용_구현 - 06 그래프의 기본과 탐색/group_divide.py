# SW Expert Academy 
# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYG3y62EcDFAVT

# Union Find 문제

import sys
sys.stdin = open("../sample_input.txt", "r")      

def get_parent(x): 
    if parent[x] != x: parent[x] = get_parent(parent[x])
    return parent[x] # 부모 노드 넣기
 
def union_parent(x, y):
    a = get_parent(x)
    b = get_parent(y)
    if a > b: parent[a] = b
    else: parent[b] = a

for test_case in range(1, int(input()) + 1):
    N,M =  map(int, input().split())
    parent = [i for i in range(N+1)]
    group = list(map(int, input().split()))
    for i in range(0, M*2, 2):
        union_parent(group[i],group[i+1])
    answer = set()
    for i in parent:
        answer.add(get_parent(i))
    print("#"+str(test_case),len(answer)-1)  