f = open('input.txt', 'r').read().splitlines()
sum = 0
for line in f:
    maxes = {'red': 0, 'green': 0, 'blue': 0}
    line = line.split(':')[1].replace(',', ';').split(';')
    for dice in line:
        dice = dice.split(' ')[1:]
        if int(dice[0]) > maxes[dice[1]]:
            maxes[dice[1]] = int(dice[0])
    values = list(maxes.values())
    power = values[0] * values[1] * values[2]
    sum += power
print(sum)