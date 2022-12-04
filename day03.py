def get_char_value(ch:str):
    if ch.isupper():
        return (ord(ch) - ord('A')) + 27
    else:
        return (ord(ch) - ord('a')) + 1


def part1():
    with open('input/day3.txt') as input_file:
        lines = input_file.readlines()
        total = 0
        for line in lines:
            total += get_char_value(set(line[:len(line)//2]).intersection(line[len(line)//2:]).pop())
        print(total)

def part1_functional():
    print(sum(get_char_value(set(line[:len(line)//2]).intersection(line[len(line)//2:]).pop()) for line in open('input/day3.txt')))

def part2():
    with open('input/day3.txt') as input_file:
        count = 0
        total = 0
        test = []
        for line in input_file:
            line = line.strip()
            test.append(line)
            if len(test) == 3:
                total += get_char_value(set.intersection(*map(set, test)).pop())
                test = []
        print(total)
        

def part2_functional():
    lines = open('input/day3.txt').readlines()
    print(sum(get_char_value(set.intersection(*map(set, map(str.strip, lines[i:i+3]))).pop()) for i in range(0, len(lines), 3)))    


part1()
part1_functional()
part2()
part2_functional()