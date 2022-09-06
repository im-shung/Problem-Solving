'''
채점 결과
정확성: 40.0
효율성: 0.0
합계: 40.0 / 100.0
'''
def solution(info, query):
    check = [[]*5 for _ in range(len(info))]
    for idx,string in enumerate(info):
        for s in string.split():
            check[idx].append(s)
    answer = []
    for q in query:
        type = q.split()
        while "and" in type:
            type.remove("and")
        idx_list = list(filter(lambda x: int(check[x][-1]) >= int(type[-1]), range(len(check))))
        cnt = 0
        for idx in idx_list:
            flag = False
            for i in range(4):
                if type[i] == '-': 
                    flag = True
                    continue
                if type[i] == check[idx][i]:
                    flag = True
                else:
                    flag = False
                    break
            if flag: 
                cnt += 1
        answer.append(cnt)
    return answer


# 실행용 코드
# info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

# check = [[]*5 for _ in range(len(info))]
# for idx,string in enumerate(info):
#     for s in string.split():
#         check[idx].append(s)
# answer = []
# for q in query:
#     type = q.split()
#     while "and" in type:
#         type.remove("and")
#     idx_list = list(filter(lambda x: int(check[x][-1]) >= int(type[-1]), range(len(check))))
#     cnt = 0
#     for idx in idx_list:
#         flag = False
#         for i in range(4):
#             if type[i] == '-': 
#                 flag = True
#                 continue
#             if type[i] == check[idx][i]:
#                 flag = True
#             else:
#                 flag = False
#                 break
#         if flag: 
#             cnt += 1
#     answer.append(cnt)
# print(answer)