# SW Expert Academy 
# 4839. [파이썬 S/W 문제해결 기본- List2] 2일차 - 이진탐색 D2
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg
   
T = int(input())

for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnt = [0,0]
    
    start = 1
    end = P
    key = Pa
    while start <= end:
        middle = start +(end - start)//2
        cnt[0]+=1
        if key == middle:
            break
        elif key < middle:
            end = middle
        else:
            start = middle
     
    start = 1
    end = P 
    key = Pb    
    while start <= end:
        middle = start +(end - start)//2
        cnt[1]+=1
        if key == middle:
            break
        elif key < middle:
            end = middle
        else:
            start = middle
        
    if cnt[0] < cnt[1]: 
        winner = "A"
    elif cnt[0] > cnt[1]:
        winner = "B"
    else:
        winner = "0"
    print("#"+str(test_case), winner)
        
