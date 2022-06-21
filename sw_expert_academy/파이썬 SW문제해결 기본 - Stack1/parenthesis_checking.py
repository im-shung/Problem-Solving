# SW Expert Academy 
# 4866. [파이썬 S/W 문제해결 기본 - Stack1] 4일차 - 괄호검사 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVHzyqqe8DFAWg&&

T = int(input())

# 괄호검사 조건
# 1️⃣ 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 함
# 2️⃣ 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 함
# 3️⃣ 괄호 사이에는 포함 관계만 존재함

for test_case in range(1, T+1):
    S = input()
    
    stack = list()
    result = 0
    idx = 0
    
    # 문자열에 있는 괄호를 차례대로 조사
    while idx < len(S):
        if S[idx] == '{' or S[idx] == '(':  # 왼쪽 괄호를 만나면 스택에 삽입
            stack.append(S[idx])
        elif S[idx] == '}' or S[idx] == ')': # 오른쪽 괄호를 만나면 
            if len(stack) == 0: # 스택이 비어있음 (조건 1 또는 조건 2에 위배)
                result = 0
                break
            elif S[idx] == '}' and stack.pop() == '{': # 스택에서 top 괄호를 삭제한 후 오른쪽 괄호와 짝이 맞는지 확인
                result = 1
            elif S[idx] == ')' and stack.pop() == '(':
                result = 1
            else: # 괄호의 짝이 맞지 않음 (조건 3에 위배)
                result = 0
                break
        idx += 1

    if (len(stack) > 0 and idx == len(S)): #  문자열 끝까지 조사한 후에도 스택에 괄호가 남아있음 (조건 1에 위배)
        result = 0
    print(f"#{test_case} {result}")