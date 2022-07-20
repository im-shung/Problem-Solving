# SW Expert Academy 
# 5120. [파이썬 S/W 문제해결 기본] 7일차 - 암호 D4
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
            print(cur.data,end=",")
            cur = cur.next
    
    # 연결리스트 길이 알아내기
    def get_count(self):
        cur = self.head
        cnt = 0
        while cur is not None:
            cnt += 1
            cur = cur.next
        return cnt
    
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
        
    def return_list(self):
        result = list()
        cur = self.head
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result    

for test_case in range(1, T+1):
    N, M, K = map(int, input().split()) # N개의 숫자, M번째 칸, K회 반복
    number = list(map(int, input().split()))
    
    # 연결 리스트 초기화    
    linked_list = LinkedList(number[0])
    for i in range(1,N):
        linked_list.append(number[i])

    cur = 0 # M칸씩 이동하는 인덱스
    # 지정 위치부터 M번째 칸을 추가
    for _ in range(K):
        l = linked_list.get_count() - 1 # 연결 리스트의 마지막 인덱스
        if cur + M == l+1:
            cur = l+1
            value = linked_list.return_one(l) + linked_list.return_one(0)
            linked_list.append(value)
        else:
            if cur + M > l+1: # 마지막 인덱스보다 더 나가면
                cur = cur + M - l - 1  # 남은 칸수는 시작 숫자부터 이어간다.
            else: 
                cur += M
            value = linked_list.return_one(cur - 1) + linked_list.return_one(cur)
            linked_list.add_node(cur,value)
    result = linked_list.return_list()
    result.reverse()
    print(f"#{test_case} {' '.join(map(str,result[:10]))}")    
    