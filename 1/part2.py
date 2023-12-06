numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

f = open('input.txt', 'r')

sum = 0
for line in f.readlines():
    indexes = {}
    for number in numbers:
        if number in line:
            indexes[line.find(number)] = numbers.index(number) + 1
    for i in range(len(line)):
        if line[i].isdigit():
            indexes[i] = int(line[i])
    indexes = dict(sorted(indexes.items()))
    calibration_value = int(list(indexes.values())[0]) * 10 + int(list(indexes.values())[-1])
    sum += calibration_value
print(sum)