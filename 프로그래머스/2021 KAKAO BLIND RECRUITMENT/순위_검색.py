'''
채점 결과
정확성: 40.0
효율성: 60.0
합계: 100.0 / 100.0
'''

def solution(info, query):
    from collections import defaultdict

    check = defaultdict(list)
    for string in info:
        s = string.split()
        for lang in [s[0], "-"]:
                for job in [s[1], "-"]:
                    for career in [s[2], "-"]:
                        for food in [s[3], "-"]:
                            check[lang+job+career+food].append(int(s[4])) # 해시테이블 사용하기
    
    # 점수별 오름차순 정렬하기
    for key in check.keys():
        check[key].sort()

    answer = []
    for q in query:
        temp = q.replace(" and ","")
        type,score = temp.split(); score = int(score)

        score_list = check[type]
        l = len(score_list)

        # 선형탐색이 아닌 이진탐색 같은 빠른 방법 쓰기
        low, high, point = 0, l - 1, l
        while low <= high:
            mid = (low+high) // 2
            if score <= score_list[mid]:
                point = mid
                high = mid - 1
            else:
                low = mid + 1
        answer.append(l-point)

    return answer


'''
TIP(https://school.programmers.co.kr/questions/25368)
1. info에 없는 조건들이 query에 있을 수 있습니다. 모든 경우의 수를 넣지 않으면 런타임 에러가 발생합니다.
2. 단순히 봐도 info 50,000개 x query 100,000개 = 50억개. 하나씩 비교해선 답이 없습니다. 해시테이블을 사용합시다.
3. 점수를 비교할 때조차 시간을 아껴야 통과합니다. 선형탐색 말고 이진탐색 같은 빠른 방법을 쓰세요!
'''