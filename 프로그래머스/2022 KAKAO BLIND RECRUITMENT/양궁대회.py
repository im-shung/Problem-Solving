from collections import Counter
import itertools

def solution(n, info):
    answer = []
    
    info = info[::-1]
    max_n = -1
    k = len(info)

    for c in itertools.combinations_with_replacement(range(k),n):
        ryan = 0
        apeach = 0
        tmp_ans = [0 for _ in range(k)]

        c = Counter(c)
        print(c)
        for i in range(k):
            if info[i] < c[i]: # 개수가 더 많으면 라이언이 승
                ryan += i
            elif info[i] != 0: # 아니면 어피치가 승
                apeach += i
                
            tmp_ans[i] = c[i]
            
        if ryan > apeach:
            diff = ryan - apeach
            if max_n < diff:
                max_n = diff
                answer = tmp_ans
                
    if answer:
        return answer[::-1]
    else:
        return [max_n]