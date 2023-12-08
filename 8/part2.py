f = open('input.txt', 'r').read().splitlines()

def check_z(pointers: []):
    for pointer in pointers:
        if pointer[2] != 'Z':
            return False
    return True

instructions = f[0]
map = {}
ghosts = []

for line in f[2:]:
    line = line.split()
    key = line[0]
    if key[2] == 'A':
        ghosts.append(key)
    L = line[2][1:4]
    R = line[3][:3]
    map[key] = (L, R)

counts = []
for ghost in ghosts:
    pointer = ghost
    steps = 0
    while pointer[-1] != 'Z':
        instruction = instructions[steps%len(instructions)]
        if instruction == 'L':
            pointer = map[pointer][0]
            steps += 1
        elif instruction == 'R':
            pointer = map[pointer][1]
            steps +=1
    counts.append(steps)
print(counts)

from math import gcd
lcm = 1
for i in counts:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)