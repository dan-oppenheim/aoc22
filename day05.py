
def run_process(input_file, reverse=False):
    stacks:dict[int, list] = {}
    in_pre = True
    in_post = False

    for line in input_file:
        if in_pre:
            for index, chunk in enumerate(line[i:i+4] for i in range(0, len(line), 4)):
                if chunk[0] == '[':
                    if index+1 not in stacks:
                        stacks[index+1] = [chunk[1]]
                    else:
                        stacks[index+1].insert(0, (chunk[1]))
                elif chunk[0] == ' ' and chunk[1] == '1':
                    in_pre = False
                    break
        elif not in_post:
            in_post = True
        else:
            parts = line.strip().split()
            target = stacks[int(parts[5])]
            source = stacks[int(parts[3])]
            count = int(parts[1])
            if reverse:
                target += reversed(source[-count:])
            else:
                target += source[-count:]
            stacks[int(parts[3])] = source[:-count]
    
    return [stacks[k][-1] for k in sorted(stacks.keys())] 
    
with open("input/day5.txt") as input_file:
    def dump(values):
        for v in values:
            print(v, sep='', end='')
        print()
        

    dump(run_process(input_file))
    input_file.seek(0)
    dump(run_process(input_file, True))