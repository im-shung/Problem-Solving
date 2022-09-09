def solution(N, stages):
    from collections import Counter
    
    fail = Counter(stages)
    users = len(stages) # 스테이지에 남아있는 사람들
    Q = []
    
    for i in range(1,N+1):
        if fail[i] == 0: rate = 0
        elif users == fail[i]: rate = 1
        else: rate = fail[i]/users
        
        Q.append([rate,i])
        
        users -= fail[i]
        
    Q.sort(key = lambda x: (-x[0],x[1]))
    answer = list(x[1] for x in Q)
    
    return answer