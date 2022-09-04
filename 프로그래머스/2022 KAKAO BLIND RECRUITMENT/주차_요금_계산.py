from collections import defaultdict

# 누적 시간 구하는 함수
def get_time(s1,s2):
    h1,m1 = map(int,s1.split(":"))
    h2,m2 = map(int,s2.split(":"))
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    if t2 > t1:
        result = t2 - t1
    else:
        result = t2 - t1 + 24 * 60
    return result

# 주차 요금 구하는 함수
def get_cost(time,fees):
    if time <= fees[0]: # 기본시간보다 작으면
        return fees[1]
    else:
        sub_cost = (time-fees[0])//fees[2]
        if (time-fees[0]) % fees[2] != 0:
            sub_cost += 1
        return fees[1] + sub_cost * fees[3]

def solution(fees, records):
    time_list = defaultdict(list)
    car_list = set()
    for i in range(len(records)):
        time,car_num,type = records[i].split()
        time_list[car_num].append(time)
        car_list.add(car_num)
    car_list = list(car_list)
    car_list.sort()

    answer = []
    for car in car_list:
        s = time_list[car]
        cost = 0
        time = 0
        if len(s) > 1:
            if len(s) % 2 != 0:
                s.append("23:59")
            for i in range(0,len(s)-1,2):
                time += get_time(s[i],s[i+1])
            cost = get_cost(time,fees)
        else: 
            time = get_time(s[0],"23:59")
            cost = get_cost(time,fees)
        answer.append(cost)
    return answer