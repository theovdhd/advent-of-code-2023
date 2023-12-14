input = open('input.txt', 'r').read().splitlines()

total = 0

copies = [1] * len(input)
for c, card in enumerate(input):
    card = card.replace('  ',' ').split(':')[1].split('|')
    winning = card[0].split(' ')[1:]
    mine = card[1].split(' ')[1:]
    matches = 0
    for w in winning:
        if w in mine:
            matches += 1
    for i in range(c+1, c+1+matches):
        copies[i] += copies[c]
        
print(sum(copies))

