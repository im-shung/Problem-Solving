from collections import defaultdict

def solution(id_list, report, k):
    idx_list = defaultdict()
    for idx,id in enumerate(id_list):
        idx_list[id] = idx

    result = defaultdict(set)
    for s in report:
        a,b = s.split(" ")
        result[b].add(a)
        
    n = len(id_list)
    answer = [0] * n
    for id in id_list:
        if len(result[id]) >= k:
            for j in result[id]:
                answer[idx_list[j]] += 1
    return answer