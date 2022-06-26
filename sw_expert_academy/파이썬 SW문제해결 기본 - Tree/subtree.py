# SW Expert Academy 
# 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg

import sys
sys.stdin = open("../sample_input.txt", "r")

T = int(input())

def get_subtree_cnt(root):
    global cnt
    for i in range(E):
        if pair[i][0] == root:
            cnt += 1
            get_subtree_cnt(pair[i][1])
       
    
for test_case in range(1, T+1):
    E, N = map(int, input().split()) # 간선의 개수 E와 노드 N
    arr = list(map(int, input().split()))
    pair = []
    for i in range(0,E*2 -1,2): # 0부터 (E*2)-2까지 2씩 증가
        parent, child = arr[i],arr[i+1]
        pair.append([parent,child])

    cnt = 1
    get_subtree_cnt(N)
    print(f"#{test_case} {cnt}")
