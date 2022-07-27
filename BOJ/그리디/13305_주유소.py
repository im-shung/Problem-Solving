n = int(input())
road = list(map(int,input().split()))
cost = list(map(int,input().split()))
result = 0
sub_result = cost[0]
# Greedy: 매 단계에서 가장 좋아보이는 것을 선택한다. 하위 문제를 풀기 전에 선택이 먼저 이루어진다.
for i in range(n-1):
    if cost[i] < sub_result: 
        sub_result = cost[i] 
    result += sub_result * road[i]
print(result)