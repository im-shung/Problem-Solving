def solution(new_id):
    # 1 
    new_id = new_id.lower() 
    # 2
    check = ["-","_","."]
    temp = ''
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in check:
            temp += i
    # 3 
    temp2 = [temp[0]]
    for i in range(1,len(temp)):
        if temp2[-1] == temp[i] == check[2]: # temp2의 마지막 값과 비교
            continue
        temp2.append(temp[i])
    # 4
    if len(temp2) > 0 and temp2[0] == check[2]: temp2 = temp2[1:]
    if len(temp2) > 0 and temp2[-1] == check[2]: temp2 = temp2[:len(temp2)-1]
    # 5 
    if len(temp2) == 0: temp2.append("a")
    # 6
    temp2 = temp2[:15]
    if temp2[-1] == check[2]: temp2 = temp2[:len(temp2)-1]
    # 7
    if len(temp2) < 3: 
        while len(temp2) < 3:
            temp2.append(temp2[-1])
    answer = ''.join(map(str,temp2))
    return answer