# SW Expert Academy 
# 5108. [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가 D3
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
    def __init__(self, data):
        self.head = Node(data)
    
    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
	
    # 특정 노드 값 리턴
    def return_one(self, index):
        node = self.get_node(index)
        return node.data
    
    # 모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
    
    # 노드 인덱스 알아내기
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node        
    
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

for test_case in range(1, T+1):
    N, M, L = map(int, input().split()) # 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L
    sequence = list(map(int, input().split())) # 수열
        
    # 연결 리스트 초기화    
    linked_list = LinkedList(sequence[0])
    for i in range(1,N):
        linked_list.append(sequence[i])
    
    for _ in range(M): # M개의 
        index, data = map(int, input().split()) # 추가할 인덱스와 숫자 정보
        linked_list.add_node(index,data) # 연결리스트에 추가
       
    print(f"#{test_case} {linked_list.return_one(L)}")
    