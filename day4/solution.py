import collections

data = []

def minutesArray():
    mins = {}
    for x in range(60):
        mins[x] = 0
    return mins

# Sample input
# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up

f = open('day4/input.txt', 'r')
for line in f:
    line = line.rstrip()
    #date = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
    date = line[1: 17]
    a=[]
    a.append(date)
    a.append(line[19:])
    data.append(a)

# ids = { 10 : {date : [minutes], 11 : { date : [min]}, ... }

data.sort()
filehandle =  open("day4/sorted.txt", "w")
for x in data:
    s = " ".join(x) + "\n"
    filehandle.writelines(s)
filehandle.close()

ids = {}
id_starts_shift = False
for x in data:
    # Guard begins shift add to ids if not in there.
    if "#" in x[1]:
        # start of shift
        id = x[1].split(" ")[1]
        id = id.strip("#")
        id_starts_shift = True
        # if id is already in ids then we are going to be counting minutes
        if id not in ids:
            m = minutesArray()
            ids[id] = m
    if "falls" in x[1]:
        #falls asleep at
        startMin = x[0].split(":")[1]
        #ids[id][startMin] += 1
    if "wakes" in x[1]:
        endMin = x[0].split(":")[1]
        for x in range(int(startMin), int(endMin)):
            ids[id][x] += 1

count = 0
for key, value in ids.items():
    c = sum(value.values())
    if c > count:
        count = c
        mid = key
print("Max time goes to ID = ", mid)

minMost = max(ids[mid], key=ids[mid].get)

# now find the id that has the highest minute slept
max_min = 0
for i in ids:
    idx = max(ids[i], key=ids[i].get)
    if ids[i][idx] > max_min:
        max_min = ids[i][idx]
        max_min_id = idx
        max_id = i

print("ID = ", max_id, "  minute = ", max_min_id, "ans = ", int(max_id) * int(max_min_id))