def part1():
    count = 0
    for p in open('input/day4.txt'):
        p1, p2 = p.strip().split(',')
        p1s, p1e = tuple(int(p) for p in p1.split('-'))
        p2s, p2e = tuple(map(int, p2.split('-')))

        

        if p1s < p2s:
            if p1e >= p2e:
                count += 1
        elif p1s > p2s:
            if p1e <= p2e:
                count += 1
        elif p1s == p2s:
            count += 1
            continue
    print(count)

def part2():
    count = 0
    for p in open('input/day4.txt'):
        p1, p2 = p.strip().split(',')
        p1s, p1e = tuple(map(int , p1.split('-')))
        p2s, p2e = tuple(map(int, p2.split('-')))

        if set.intersection(set(i for i in range(p1s, p1e+1)), set(i for i in range(p2s, p2e+1))):
            count += 1
    print(count)

part1()
part2()