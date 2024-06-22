# import dataset
filename = "IMDB-Movie-Data.csv"
f = open(filename, "r")
line = f.read()
lineLs = line.split('\n')
cl_data = []
for l in lineLs:
    cl_data.append(l.split(","))
del cl_data[0]
del cl_data[-1]
f.close()

# Q1
def Question1():
    data = []
    for r in cl_data:
        # create list containing movies in 2016
        if r[5] == "2016":
            data.append(r)
    # sort
    data.sort(key=lambda x:x[7], reverse=True)
    top1, top2, top3 = data[0][1], data[1][1], data[2][1]
    print("Q1: \ntop1:", top1)
    print("top2:", top2)
    print("top3: %s\n" %top3)

# Q2
def Question2():
    directors = {}
    data = cl_data
    # director list
    dirLs = [d[3] for d in data]
    for d in dirLs:
        if not d in directors:
            directors[d] = 1
        else:
            directors[d] += 1
    sorted_dir = dict(sorted(directors.items(), key=lambda x:x[1], reverse=True))
    #存取 sorted_dir 中 keys() 的第一項
    top1 = list(sorted_dir.keys())[0]
    print("Q2:\nThe director: %s \n" %top1)

# Q3
def Question3():
    data = cl_data
    for i in range(len(data)):
        # 將人名用 "|" 分割
        data[i][4] = data[i][4].split("|")
        # 分割符號 "|" 時會使有些名字第一格出現空格，因此用strip消除
        for j in range(len(data[i][4])):
            data[i][4][j] = data[i][4][j].strip()
    # actors dictionary stores the total revenue
    actors = {}
    for r in data:
        for a in r[4]:
            if a not in actors:
                actors[a] = 0
            if r[9] != "":
                actors[a] += float(r[9])
    sorted_actors = dict(sorted(actors.items(), key=lambda x:x[1], reverse=True))
    richest_actor = list(sorted_actors.keys())[0]
    print("Q3:\nThe actor: %s\n" % richest_actor)

    return data

# Q4
def Question4(data):
    sumRate = 0
    m = 0
    for r in data:
        for a in r[4]:
            if a == "Emma Watson":
                sumRate += float(r[7])
                m += 1
    # calculate average rate 
    avgRate = sumRate / m
    print("Q4:\nAverage rating: %.3f \n" % avgRate)

# Q5
def Question5(data):
    # actors dictionary stores how many movies an actor plays
    actors = {}
    for r in data:
        # actors list index is 4
        for a in r[4]:
            if a not in actors:
                actors[a] = 1
            else:
                actors[a] += 1
    sorted_actors = sorted(actors.items(), key=lambda x:x[1], reverse=True)
    top4 = []
    for i in range(4):
        top4.append(sorted_actors[i][0])
    print("Q5:\ntop1: %s\ntop2: %s\ntop3: %s\ntop4: %s\n" % (top4[0], top4[1], top4[2], top4[3]))

# Q6
def Question6(data):
    # create a director-actor dictionary
    dir_ac = {}
    for r in data:
        dir = r[3]
        for a in r[4]:
            # partner
            par = dir + " - " + a
            if par not in dir_ac:
                dir_ac[par] = 1
            else:
                dir_ac[par] += 1
    s_dir_ac = sorted(dir_ac.items(), key=lambda x:x[1], reverse=True)
    print("Q6:")
    # print out the top7 pairs
    for i in range(7):
        print("top%d: %s" %(i+1, s_dir_ac[i][0]))
    print()

# Q7
def Question7(data):
    # create director dictionary
    dir = {}
    dirLs = [r[3] for r in data]
    for d in dirLs:
        # director
        if d not in dir:
            dir[d] = []
    for r in data:
        for a in r[4]:
            if a not in dir[r[3]]:
                dir[r[3]].append(a)
    # 將values中的list改為其長度
    for n in list(dir.keys()):
        dir[n] = len(dir[n])
    # sorted
    sorted_dir = sorted(dir.items(), key=lambda x:x[1], reverse=True)
    print("Q7:")
    for i in range(3):
        print("top%d: %s" %(i+1, sorted_dir[i][0]))
    print()

# Q8
def Question8(data):
    # split the genre of movies
    for i in range(len(data)):
        data[i][2] = data[i][2].split("|")

    actor = {}
    for r in data:
        for n in r[4]:
            if n not in actor:
                actor[n] = []
            # append genre
            for g in r[2]:
                if g not in actor[n]:
                    actor[n].append(g)
    # 將 actor.values() 改為 list 長度
    for a in list(actor.keys()):
        actor[a] = len(actor[a])
    # sorted
    sorted_actors = sorted(actor.items(), key=lambda x:x[1], reverse=True)
    print("Q8:")
    for i in range(6):
        print("top%d: %s" %(i+1, sorted_actors[i][0]))
    print()

# Q9
def Question9(data):
    # 存放演出電影年分的 dictionary
    actors = {}
    for r in data:
        for a in r[4]:
            if a not in actors:
                actors[a] = []
            actors[a].append(int(r[5]))
    # calculate gap year
    for a in list(actors.keys()):
        if len(actors[a]) > 1:
            actors[a] = max(actors[a]) - min(actors[a])
        else:
            actors[a] = 0
    sorted_actors = sorted(actors.items(), key=lambda x:x[1], reverse=True)
    print("Q9:")
    for i in range(3):
        print("top%d: %s" %(i+1, sorted_actors[i][0]))


# execute funtions
Question1()
Question2()
data = Question3()
Question4(data)
Question5(data)
Question6(data)
Question7(data)
Question8(data)
Question9(data)