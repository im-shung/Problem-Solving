import sys
sys.stdin = open("sample_input.txt", "r")
N = int(sys.stdin.readline().strip())
tree = {}
for _ in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left,right]

def preorder(root): # 전위 순회 (루트) (왼쪽 자식) (오른쪽 자식)
    if root != '.':
        print(root,end="")
        preorder(tree[root][0]) 
        preorder(tree[root][1]) 

def inorder(root): # 중위 순회 (왼쪽 자식) (루트) (오른쪽 자식)
    if root != '.':
        inorder(tree[root][0]) 
        print(root,end="") 
        inorder(tree[root][1])        

def postorder(root): # 후위 순회  (왼쪽 자식) (오른쪽 자식) (루트)
    if root != '.':
        postorder(tree[root][0]) 
        postorder(tree[root][1])   
        print(root,end="")     
preorder('A'); print()
inorder('A'); print()
postorder('A')
    