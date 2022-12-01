
class Data:
    def __init__(self, day:int) -> None:
        with open(f"input/day{day}.txt") as input_file:
            self.raw_lines = [line.strip() for line in input_file]

def count_and_order_calories(data:Data):
    counts = []
    current_count = 0
    for line in data.raw_lines:
        if line:
            current_count += int(line)
        else:
            counts.append(current_count)
            current_count = 0
    counts.sort(reverse=True)
    return counts

def part1(data:Data):
    print(f"The highest number of calories held is {count_and_order_calories(data)[0]}")

def part2(data:Data):
    print(f"The calories held by the three elves with the most is {sum(count_and_order_calories(data)[:3])}")

if __name__ == '__main__':
    data = Data(1)
    part1(data)
    part2(data)

