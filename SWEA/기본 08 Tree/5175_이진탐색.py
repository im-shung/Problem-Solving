# SW Expert Academy 
# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg

import sys
sys.stdin = open("../sample_input.txt", "r")

T = int(input())

# 트리 문제에서 추가적인 노드 삽입이나, 삭제가 없으면 리스트를 이용하여 구현

# 이진 탐색 트리는 어떤 경우에도 저장된 값이 
# 왼쪽 서브트리의 '루트 <현재 노드 <오른쪽 서브 트리의 루트' 규칙을 만족한다.

# 중위순회(left -> root -> right)
def binary_search(v):
    global cnt, result
    if v <= N: 
        # 왼쪽 자식 노드 방문
        binary_search(v  * 2) 
        # 더 이상 못 가면 값 넣기
        if v == 1: # 조상 노드 값 담기
            result[0] = cnt
        elif v == N//2: # N//2 노드에 저장된 값
            result[1] = cnt
        # cnt 증가
        cnt += 1 
        # 오른쪽 자식 노드 방문
        binary_search(v  * 2 + 1) 

for test_case in range(1, T+1):
    N = int(input()) 
    cnt = 1 # 노드에 저장된 값 (1~N)
    result = [0,0] # [루트노드에 저장된 값, N//2 노드에 저장된 값]
    binary_search(1)
    print(f"#{test_case} {' '.join(map(str,result))}")

