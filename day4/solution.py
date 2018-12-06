from datetime import datetime
data = []

f = open('day4/input.txt', 'r')
for line in f:
    line = line.rstrip()
    date = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
    a=[]
    a.append(date)
    a.append(line[19:])
    data.append(a)

data.sort()
for x in data:
    print(x[0])
print("done")