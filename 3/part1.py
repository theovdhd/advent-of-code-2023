class Number:
    def __init__(self, value, line, start, end):
        self.value = value
        self.line = line
        self.start = start
        self.end = end
        self.part = False

    def print(self):
        print(self.value + " at " + str(self.line) + " from " + str(self.start) + " to " + str(self.end))

class Symbol:
    def __init__(self, value, line, pos):
        self.value = value
        self.line = line
        self.pos = pos

    def print(self):
        print(self.value + " at " + str(self.line) + " at " + str(self.pos))

f = open('input.txt', 'r').read().splitlines()
line_number = 0


numbers =[]
symbols = []
integers = [str(i) for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
numberScan = False
for line_number, line in enumerate(f):
    max = len(line)
    for i, char in enumerate(line):
        if char in integers:
            if not numberScan:
                # we've found a number
                # START SCAN
                numberScan = True
                start = i
            elif numberScan:
                if i == max-1:
                    print(max)
                    print('weeb')
                    # we've reached the end of the line
                    # END SCAN
                    numberScan = False
                    # we need to save the end index
                    end = i
                    # we need to create a number object
                    number = Number(line[start:end+1], line_number, start, end)
                    numbers.append(number)
                    print(number.value)
                    start = None
                # we're still scanning
                # CONTINUE SCAN
                pass
        if char not in integers and numberScan:
            # we've reached the end of the number
            numberScan = False
            # we need to save the end index
            end = i
            # we need to create a number object
            number = Number(line[start:end], line_number, start, end)
            numbers.append(number)
            start = None
        if char not in integers and not numberScan:
            if char != '.':
                # we've found a sumbol
                symbol = Symbol(char, line_number, i)
                symbols.append(symbol)
sum = 0
for number in numbers:
    for symbol in symbols:
        if symbol.line >= number.line - 1 and symbol.line <= number.line + 1:
            if symbol.pos >= number.start - 1 and symbol.pos <= number.end:
                print("Symbol " + symbol.value + " is in number " + number.value + " at line " + str(number.line) + " from " + str(number.start) + " to " + str(number.end))
                number.part = True
    if number.part:
        sum += int(number.value)
print(sum)