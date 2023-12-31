input = open('input.txt', 'r').read().splitlines()

total = 0 
for card in input:
    card = card.replace('  ',' ').split(':')[1].split('|')
    winning = card[0].split(' ')[1:]
    mine = card[1].split(' ')[1:]
    points = 0
    for w in winning:
        if w in mine:
            if points == 0:
                points = 1
            else:
                points *= 2
    total += points
print(total)