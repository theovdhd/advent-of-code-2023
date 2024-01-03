f = open('input.txt', 'r').readlines()

seeds = f[0][7:].strip().split(' ')

maps = {}

for line in f[1:]:
    if line != '\n':
        if line[-5:] == 'map:\n':
            map_name = line.strip().split(' ')[0]
            maps[map_name] = []
        else:
            line = [int(i) for i in line.strip().split(' ')]
            maps[map_name].append([line[0], line[1], line[1]+line[2]-1, line[0]-line[1]])

lowest = 9999999999999
for next in seeds:
    next = int(next)
    for k, v in maps.items():
        for map in v:
            if map[1] <= next <= map[2]:
                next = next + map[3]
                break

    if next < lowest:
        lowest = next
print(lowest)