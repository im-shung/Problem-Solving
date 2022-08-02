import sys
input = sys.stdin.readline
moves = [(1,0),(0,1),(-1,0),(0,-1)]
t = int(input())
room = [[0] * t for _ in range(t)]
students = [0] * (t*t) 
likes_zip = [0] * (t*t) 
for i in range(t*t):
    student, *like = map(int,input().split())
    students[i] = student
    likes_zip[i] = like
for i in range(t*t):
    student, likes = students[i], likes_zip[i]
    tmp = []
    for i in range(t):
        for j in range(t):
            if room[i][j] == 0:
                empty = 0
                friend = 0
                for _x,_y in moves:
                    dx = i + _x
                    dy = j + _y
                    if 0 <= dx < t and 0 <= dy < t:
                        if room[dx][dy] == 0:
                            empty +=1
                        else:
                            if room[dx][dy] in likes: friend += 1                        
                tmp.append([i,j,empty,friend])
    tmp.sort(key = lambda x:(-x[3],-x[2],x[0],x[1]))
    x,y = tmp[0][0],tmp[0][1]
    room[x][y] = student
sum = 0  
for i in range(t):
    for j in range(t):
        friend = 0
        student = room[i][j]
        idx = int(students.index(student))
        for _x,_y in moves:
            dx = i + _x
            dy = j + _y
            if 0 <= dx < t and 0 <= dy < t:
                if room[dx][dy] in likes_zip[idx]: friend += 1
        if friend != 0: sum += 10**(friend-1)
print(sum)