# SW Expert Academy 
# 5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기 D3
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

    def return_list(self):
        result = list()
        cur = self.head
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result

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
        
    # 특정 위치에 리스트 삽입하기        
    def find_bigger_and_add_list(self, linked_list,N):
        # print(f"N={N}")
        index = 0
        front_node = linked_list.get_node(0) # 수열의 첫 데이터
        rear_node = linked_list.get_node(N-1) # 수열의 마지막 데이터
        node = self.head
        # print(f"node={node.data}",end=", "); print(f"front_node={front_node.data}")
        while node is not None and node.data <= front_node.data:
            index += 1
            node = node.next
        # print(f"index={index}")    
        
        node = self.get_node(index)
        pre_node = self.get_node(index-1)
        
        if pre_node.data < front_node.data and index == N: # 끝에 도달한 경우
            pre_node.next = front_node
            return
        if index == 0:
            rear_node.next = self.head
            self.head = front_node
            return
        
        pre_node.next = front_node
        rear_node.next = node
    
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # 수열의 길이 N, 수열 개수 M
    sequences = [list(map(int, input().split())) for _ in range(M)]
    linked_lists = list()
    
    # 모든 수열을 연결리스트로 만들기
    for r in range(M):
        linked_lists.append(LinkedList(sequences[r][0]))
        for c in range(1,N):
            linked_lists[r].append(sequences[r][c])
    
    for i in range(1, M):
        # print(f"{i}번째 중")
        # print(linked_lists[i-1].print_all())
        linked_lists[i-1].find_bigger_and_add_list(linked_lists[i], N) 
        linked_lists[i] = linked_lists[i-1]
    
    
        
    result = linked_lists[M-1].return_list()
    result.reverse()
    print(f"#{test_case} {result[:10]}")
    