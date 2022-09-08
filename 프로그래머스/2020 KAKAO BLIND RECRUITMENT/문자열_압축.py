# 리스트를 n크기만큼 분할하는 함수
def list_chunk(lst,n):
    return [lst[i:i+n] for i in range(0,len(lst),n)]

def solution(s):
    ans = [len(s)]
    for n in range(1,len(s)//2+1):
        stack = []
        for i in range(0, len(s), n):
            # 먼저 문자열을 압축할 단위로 자릅니다.
            if stack and stack[-1][1] == s[i:i+n]: 
                stack[-1][0] += 1 # 만약 스택 top 항목이 잘라낸 문자열과 같으면 top의 cnt를 증가시킵니다. 
            else:
                stack.append([1,s[i:i+n]]) # 다르다면 스택에 [1, 문자열] 형태로 집어넣습니다.
        
        # 문자열을 모두 스택에 집어넣었으면 카운트를 시작합니다.
        answer = 0
        for item in stack:
            if item[0] != 1:
                answer += len(str(item[0])) # cnt가 1이 아니면 숫자의 길이만큼도 증가시킵니다.
            answer += len(item[1]) # cnt가 1이면 문자열의 길이만큼만 증가시킵니다.
        ans.append(answer)
        
    return min(ans)
