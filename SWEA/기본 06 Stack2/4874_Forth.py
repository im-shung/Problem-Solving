# SW Expert Academy 
# 4874. [파이썬 S/W 문제해결 기본 - Stack2] 5일차 - Forth D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg

# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    arr = list(input().split())

    operators = ['+','-','*','%','/']
    stack = list()
    result = 0
    
    for idx in range(len(arr)):
        if arr[idx] == '.':
            result = stack.pop()
        elif arr[idx] in operators: # 연산자
            if len(stack) < 2: # 스택에 계산할 피연산자 2개가 없다면, error
                result = "error"
                break
            else: # 스택에 계산할 피연산자 2개가 있다면, 계산 후 결과를 push
                a1 = int(stack.pop()); a2 = int(stack.pop())
                if arr[idx] == '+': str = a2 + a1
                elif arr[idx] == '-': str = a2 - a1
                elif arr[idx] == '/': str = a2 // a1 # '/'의 소수점 주의!
                elif arr[idx] == '*': str = a2 * a1
                elif arr[idx] == '%': str = a2 % a1
                stack.append(str)
                
                # eval 함수를 사용할 수도 있음
                # str = f"{a2}{arr[idx]}{a1}"
                # stack.append(eval(str))
                
        else: # 피연산자
            stack.append(arr[idx])
            
    if len(stack) > 0:
        result = "error"
    print(f"#{test_case} {result}")