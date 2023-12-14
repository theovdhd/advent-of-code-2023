universe = open('input.txt', 'r').read().splitlines()
expansion = 1000000

galaxies = []
empty_rows = list(range(len(universe)))
empty_cols = list(range(len(universe)))
def dist(g1, g2):
    return abs(g2[0]-g1[0]) + abs(g2[1]-g1[1])
for r, line in enumerate(universe):
    empty = True
    for c, char in enumerate(line):
        if char == '#':
            empty = False
            galaxies.append((r, c))
            if r in empty_rows:
                empty_rows.remove(r)
            if c in empty_cols:
                empty_cols.remove(c)

exp_galaxies = []
for x,y in galaxies:
    exp_galaxy = [x, y]
    for r in empty_rows:
        if r < x:
            exp_galaxy[0] += expansion - 1
    for c in empty_cols:
        if c < y:
            exp_galaxy[1] += expansion - 1
    exp_galaxies.append(exp_galaxy)

sum = 0

for i, g in enumerate(exp_galaxies):
    for j, h in enumerate(exp_galaxies[i+1:]):
        add = dist(g, h)
        sum += add

print(sum)


