template = """
def part1():
    print("In part1")

def part2():
    print("In part2")

if __name__ == '__main__':
    part1()
    part2()
"""

for day in range(1, 25):
    file_name = f"python/day{day:02}.py"
    with open(file_name, 'w') as out_file:
        print(template, file=out_file)
