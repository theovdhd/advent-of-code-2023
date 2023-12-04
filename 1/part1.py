f = open('input.txt', 'r')
sum = 0
for line in f.readlines():
    num = ''
    for char in line:
        if char.isdigit():
            num += char
    final = int(num[0]) * 10 + int(num[-1])
    sum += final
print(sum)
