import collections

data = []

f = open('day2/input.txt', 'r')
for line in f:
    data.append(line.rstrip())

twos = 0
threes = 0

for x in data:
    d = collections.Counter(x).most_common(3)
    if(len(d)):
        for c in d:
            if c[1] == 2:
                twos += 1
                break
        for c in d:
            if c[1] == 3:
                threes += 1
                break

print("Answer = ", twos * threes)


for x in data:
    for y in data:
        count = 0
        result = []
        if x == y:
            continue
        for a, b in zip(x, y):
            if count > 1:
                break
            if a != b:
                count += 1
                continue
            result.append(a)

        if count == 1:
            print(''.join(result))