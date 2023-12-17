f = open('input.txt', 'r').readlines()

seeds = f[0][7:].strip().split(' ')

maps = {}
dag = {}
calc_map = {}

for line in f[1:]:
    if line != '\n':
        if line[-5:] == 'map:\n':
            map_name = line.strip().split(' ')[0]
            maps[map_name] = []
            dag[map_name.split('-')[0]] = map_name.split('-')[2]
        else:
            maps[map_name].append(line.strip().split(' '))

type = 'seed'
while type in dag:
    dest = dag[type]
    map_name = type + '-to-' + dest
    print(map_name)
    type_map = {}
    for map in maps[map_name]:
        print(map)
        dest_range_start = int(map[0])
        source_range_start = int(map[1])
        range_length = int(map[2])
        for i in range(int(range_length)):
            type_map[source_range_start + i] = dest_range_start + i
    calc_map[type + '-to-' + dag[type]] = type_map
    type = dag[type]

final = {}
for seed in seeds:
    type = 'seed'
    n = int(seed)
    while type != 'location':
        dest = dag[type]
        map_name = type + '-to-' + dest
        if n in calc_map[map_name].keys():
            n = calc_map[map_name][n]
        type = dest
    final[seed] = n

print(min(final.values()))
'''
The first line has a destination range start of 50, 
a source range start of 98, and a range length of 2. 
This line means that the source range starts at 98 and 
contains two values: 98 and 99. The destination range is
the same length, but it starts at 50, so its two values
are 50 and 51. With this information, you know that seed 
number 98 corresponds to soil number 50 and that seed number 
99 corresponds to soil number 51.

The second line means that the source range starts at 50 
and contains 48 values: 50, 51, ..., 96, 97. This corresponds
to a destination range starting at 52 and also containing 48
values: 52, 53, ..., 98, 99. So, seed number 53 corresponds 
to soil number 55.
'''