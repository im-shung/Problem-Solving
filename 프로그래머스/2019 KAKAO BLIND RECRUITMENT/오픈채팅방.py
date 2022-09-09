def solution(record):
    from collections import defaultdict
    chat = []
    name_list = defaultdict(str)
    for r in record:
            string = r.split()
            if string[0] != 'Leave':
                type,user_id,nickname = string[0],string[1],string[2]
                name_list[user_id] = nickname
            else:
                type,user_id = string[0],string[1]
                
            if type == 'Enter' or type == 'Leave':
                chat.append([user_id,type])
    answer = []
    for user_id,type in chat:
        if type == 'Enter':
            answer.append(name_list[user_id]+"님이 들어왔습니다.")
        else:
            answer.append(name_list[user_id]+"님이 나갔습니다.")
    return answer