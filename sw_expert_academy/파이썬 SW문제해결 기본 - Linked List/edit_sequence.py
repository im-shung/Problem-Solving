# SW Expert Academy 
# 5122. [파이썬 S/W 문제해결 기본] 7일차 - 수열 편집 D4
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ1r6qfkDFAWg

import sys
sys.stdin = open("../sample_input.txt", "r")

T = int(input())

# 노드 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 연결리스트 클래스         
class LinkedList:
    def __init__(self,data):
        self.head = Node(data)
        
    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
    
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data,end=",")
            cur = cur.next

    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            if(node is None):
                return -1
            cnt += 1
            node = node.next
        return node 
    
    # 노드 삭제하기
    def delete_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index -1:
            cnt += 1
            node = node.next
        pre_node = node
        node = node.next
        pre_node.next = node.next
        node.next = None
    
    # 특정 위치에 노드 삽입하기        
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        
    # 노드 값 변경하기
    def change_node(self, index, value):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        node.data = value 
        

for test_case in range(1, T+1):
    N, M, L = map(int, input().split()) # 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L
    number = list(map(int, input().split()))
    edit_string = list()
    for _ in range(M):
        edit_string.append(list(map(str,input().split())))
    
    # 연결 리스트 초기화    
    linked_list = LinkedList(number[0])
    for i in range(1,N):
        linked_list.append(number[i])
    for i in range(M):
        if len(edit_string[i]) == 3:
            op, a, b = edit_string[i]
        elif len(edit_string[i]) == 2:
            op, a = edit_string[i]
        
        # op에 따라서 각각 처리
        a = int(a); b = int(b)
        if op == "I":
            linked_list.add_node(a,b) # a 인덱스에 b값 넣기
        elif op == "D":
            linked_list.delete_node(a)
        elif op == "C":
            linked_list.change_node(a,b)
            
    result = linked_list.get_node(L)
    if result != -1: result = result.data
    print(f"#{test_case} {result}")
            