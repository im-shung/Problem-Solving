def solution(relation):
    # 유일성: 키에 대해 카운팅을 했을 때 중복이 없는 경우
    # 최소성: 키의 속성들 중 하나라도 제외했을 때 유일성이 깨지는 것을 의미
    from collections import defaultdict,Counter
    import itertools
   
    row, col = len(relation), len(relation[0])
    
    # column index 전체 조합 구하기
    combi_list = []
    for i in range(1,col+1):
        combi_list.extend(itertools.combinations(range(col),i)) 
  
    # 유일성
    unique = []
    for combi in combi_list:
        # 각 index 조합의 모든 column들을 tuple로 생성, 리스트로 감싸기
        tmp = [tuple([item[i] for i in combi]) for item in relation]
        
        # tmp를 set()으로 감싼 후에 길이가 전체 row의 개수와 동일한 경우는 중복이 없었다는 얘기 (유일성)
        # unique 리스트에 담기 
        if len(set(tmp)) == row:
            unique.append(combi)
    
    # 최소성
    answer, n = set(unique),len(unique)
    for i in range(n):
        for j in range(i+1,n):
            # unique 리스트에서 하나씩 뽑고, 그 뒤의 모든 요소들과 "교집합"을 구해서 길이를 비교한다.
            # "교집합"의 길이가 같은 경우는 최소성을 만족하지 못하기 때문에 리스트에서 제거한다.
            if len(unique[i]) == len( set(unique[i]) & set(unique[j] )):
                answer.discard(unique[j]) # list.remove()의 경우 지우려는 요소가 없으면 KeyError가 발생하므로 discard로 제거
    return len(answer)