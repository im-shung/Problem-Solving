import sys
input = sys.stdin.readline

n,x = map(int,input().split())
visits = list(map(int,input().split()))
'''
Sliding Window(슬라이딩 윈도우): n개의 원소를 가지는 배열이 존재하고, x개의 창문을 가진다.
    0) 창문을 왼쪽부터 한 칸씩 오른쪽으로 이동
    1) 매 순간 창문 안에서의 정보 유출 (예: 합 구하기)
'''
if max(visits) == 0: print("SAD")
else:
    max_visits = sum(visits[:x])
    sub_sum = max_visits
    cnt = 1
    for i in range(x,n):
        sub_sum += visits[i] # 오른쪽으로 한 칸 이동 
        sub_sum -= visits[i-x] # 맨 왼쪽 한 칸 삭제
        if sub_sum > max_visits:
            max_visits = sub_sum
            cnt = 1
        elif sub_sum == max_visits:
            cnt += 1
    print(max_visits)
    print(cnt)