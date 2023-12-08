f = open('input.txt', 'r').read().splitlines()

instructions = f[0]
map = {}
for line in f[2:]:
    line = line.split()
    key = line[0]
    L = line[2][1:4]
    R = line[3][:3]
    map[key] = (L, R)

pointer = 'AAA'
steps = 0
while pointer != 'ZZZ':
    instruction = instructions[steps%len(instructions)]
    if instruction == 'L':
        pointer = map[pointer][0]
        steps += 1
    elif instruction == 'R':
        pointer = map[pointer][1]
        steps +=1

print(steps)