# Determine which games would have been possible if the bag had been
# loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.

limits = {'red': 12, 'green': 13, 'blue': 14}

def check(line):
    line = line.replace(',', ';').split(';')
    for dice in line:
        dice = dice.split(' ')[1:]
        if int(dice[0]) > limits[dice[1]]:
            return False
    return True

f = open('input.txt', 'r').read().splitlines()
sum = 0
for line in f:
    ID, line = line.split(':')
    ID = int(ID.split(' ')[1])
    possible = check(line)
    if possible:
        sum += ID
print(sum)