# SW Expert Academy 
# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임 D3
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT
    
import sys
sys.stdin = open("../sample_input.txt", "r")      
      
T = int(input())

def check_baby_gin(arr):
    for i in range(len(arr)):
        if arr[i] >= 3:
            return True
        if i+3 < len(arr) and arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:
            return True
    return False

for test_case in range(1, T+1):
    arr = list(map(int,input().split()))
    
    count1 = [0] * 12
    count2 = [0] * 12
    j = 0
    winner = 0
    for i in range(0,12,2):
        player1 = arr[i]; player2 = arr[i+1]
        count1[player1] += 1; 
        if i >= 2 and check_baby_gin(count1): 
            winner = 1
            break
        count2[player2] += 1
        if i >= 2 and check_baby_gin(count2): 
            winner = 2
            break
    print(f"#{test_case} {winner}")     