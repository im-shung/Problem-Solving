# SW Expert Academy 
# 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVHzyqqe8DFAWg&&

import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

def drc(S):
    global result
    if (len(S) < 2 ): 
        result = len(S)
        return
    i = 0
    while i < len(S)-1:
        if S[i] == S[i+1]:
            S = S[0:i] + S[i+2:len(S)]
            drc(S)
            return
        else:
            i += 1
    if (i == len(S)-1): 
        result = len(S)
        return
    

for test_case in range(1, T+1):
    S = input()
    drc(S)
    print(f"#{test_case} {result}")
    