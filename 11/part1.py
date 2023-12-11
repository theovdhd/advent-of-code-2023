universe = open('input.txt', 'r').read().splitlines()

width = len(universe[0])

# expand vertically
def checkLine(line):
    for char in line:
        if char != '.':
            return False
    return True

indexes = []
for i in range(len(universe)):
    line = universe[i]
    if checkLine(line):
        indexes.append(i)

expanded = universe

offset = 0
for i in indexes:
    expanded.insert(i + offset, '.'*width)
    offset += 1

# expand horizontically
def insert(s, pos, add):
     return s[:pos] + add + s[pos:]

length = len(expanded)
indexes = []
for i in range (width):
    # iter over columns
    # i = column index
    column = []
    for j in range(length):
        column.append(expanded[j][i])
    if checkLine(column):
        indexes.append(i)
offset = 0
for i in indexes:
    for j in range(length):
        expanded[j] = insert(expanded[j], i + offset, '.')
    offset += 1
# expansion finished

length, width = len(expanded), len(expanded[0])

# find all the galaxies, put their coords in a list
# i is Y (line) coord and j is X (column) coord
galaxies = []
for i in range(length):
    for j in range(width):
        if expanded[i][j] == '#':
            galaxies.append((i, j))

total = 0

for p in galaxies:
    for q in galaxies:
        distance = abs(p[0] - q[0]) + abs(p[1] - q[1])
        total += distance
print(int(total/2))