data = []
cover = set()
f = open('day3/input.txt', 'r')
for line in f:
    line = line.rstrip()
    a = line.split(" ")
    a[0] = a[0].strip("#")
    a[2] = a[2].strip(":")
    a[2] = a[2].split(",")
    a[3] = a[3].split("x")
    data.append(a)

fabric = []

for i in range(1000):
    fabric.append([])
    for j in range(1000):
        fabric[i].append(0)

# here is sample data to mark with 1's
#1 @ [850, 301] [23, 12]
for line in data:
    c1 = int(line[2][0]) # starting col
    r1 = int(line[2][1]) # starting row
    c2 = int(line[3][0]) # number of cols it takes up
    r2 = int(line[3][1]) # number of rows it takes up
    for x in range(c1, c1 + c2):
        for y in range (r1, r1 + r2):
            if fabric[x][y] == 0:
                fabric[x][y] = line[0]
            else:
                fabric[x][y] = "X"
                cover.add((x,y))

print(len(cover))

# Part 2 finds ID that doesn't overlap
for line in data:
    c1 = int(line[2][0]) # starting col
    r1 = int(line[2][1]) # starting row
    c2 = int(line[3][0]) # number of cols it takes up
    r2 = int(line[3][1]) # number of rows it takes up
    overlaps = False
    for x in range(c1, c1 + c2):
        for y in range(r1, r1 + r2):
            if fabric[x][y] == line[0]:
                continue
            else:
                overlaps = True
                break
    if overlaps == False:
        print("ID that doesn't overlap is ", line[0])
    