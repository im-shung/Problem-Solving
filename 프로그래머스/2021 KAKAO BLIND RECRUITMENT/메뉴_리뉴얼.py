def solution(orders, course):
    from collections import Counter
    import itertools

    answer = []

    for c in course:
        '''
        [step1]
        ('A', 'C')와 ('C', 'A')는 같은경우 이므로 이런 경우가 안생기게 하려면 조합에 사용되는 자료가 정렬되어 있어야함.
        -> 문자열은 sorted('문자열')을 사용
        '''
        menu = []
        for o in orders:
            menu += list(itertools.combinations(sorted(o),c))

        '''
        [step2]
        코스요리 메뉴별 시킨 사람수 카운트를 정렬함 (Counter클래스의 most_common() 사용)
        '''
        menu_list = Counter(menu).most_common() # [(('A','C'),1), (('A', 'D'), 1) ···]
        max = 2
        for menu,cnt in menu_list:
            if cnt < max: break
            else:
                answer.append(''.join(menu))
                if cnt > max: max = cnt
    answer.sort()
    return answer