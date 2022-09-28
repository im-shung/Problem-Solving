from collections import defaultdict


queries	= [[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]	
# result = 16

###########################################
# 풀이1 
def get_size(n):
    i = 1
    while i < n:
        i *= 2
    return i

def solution(queries):
    arr = defaultdict(list)
    cnt = 0

    for n,num in queries: # 배열 번호, 넣는 원소 개수
        pre_num, len_arr = arr[n] # 원소 개수, 배열 크기
        new_num = pre_num + num

        if new_num == num: # 기존 배열에 원소가 없기 때문에 복사 x
            arr[n] = [get_size(new_num),new_num]
        elif new_num <= len_arr:
            arr[n] = [get_size(new_num),new_num]
        elif new_num > len_arr:
            cnt += pre_num
            arr[n] = [get_size(new_num),new_num]
    print(cnt)        

    answer = cnt
    return cnt
###########################################


###########################################
# 풀이2
# 해몽
def solution2(queries):
    ans = 0
    sizes = [(0, 1) for _ in range(1001)] # (load count, capacity)

    for a,b in queries:
        
        cnt, capacity = sizes[a]
        nxt, org = cnt + b, capacity
        
        while nxt > capacity:
            capacity *= 2
            
        if org != capacity:
            ans += cnt
        
        sizes[a] = (nxt, capacity)
    print(ans)
###########################################