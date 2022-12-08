
def run_process(input_file, chunked=False):
    stacks:dict[int, list] = {}
    # This algorithm uses a single pass over the input file, 
    # so it needs to know when it's processing the initial stack
    # state and when it's processing the commands
    # in_pre indicates it's doing the former and in_post the latter.
    # When the first line without a '[' character is found, in_pre
    # is set to False, which causes the next empty line to be skipped
    # and in_post set to True, at which point each line is treated as 
    # a command
    in_pre = True
    in_post = False

    for line in input_file:
        if in_pre:
            # Each line is split into 4 character chunks, which will be in
            # the format '[\c] ' or will be empty. The characters in the chunks are
            # stored in their stack index
            for index, chunk in enumerate(line[i:i+4] for i in range(0, len(line), 4)):
                if chunk[0] == '[':
                    if index+1 not in stacks:
                        stacks[index+1] = [chunk[1]]
                    else:
                        stacks[index+1].insert(0, (chunk[1]))
                # if the first chunk starts with ' 1' then we're at the labels
                # line and done with processing the initial stacks
                elif chunk[0] == ' ' and chunk[1] == '1':
                    in_pre = False
                    break
        elif not in_post:
            in_post = True
        else:
            # each line is now a command. The line gets split into space-delimited
            # chunks and the source stack, target stack and how many to move
            # are determined
            parts = line.strip().split()
            target = stacks[int(parts[5])]
            source = stacks[int(parts[3])]
            count = int(parts[1])
            # If we're moving the top of the stack in a single block
            # then we just grab the the last `count` items and move them
            # Otherwise we have to reverse their order, to simulate moving
            # them a block at a time
            if chunked:
                target += source[-count:]                
            else:
                target += reversed(source[-count:])
            # finally, remove the moved blocks from their stack 
            stacks[int(parts[3])] = source[:-count]
    
    # Takes the top of each stack and puts them into a list
    return [stacks[k][-1] for k in sorted(stacks.keys())] 
    
with open("input/day5.txt") as input_file:
    def dump(values):
        for v in values:
            print(v, sep='', end='')
        print()
        

    dump(run_process(input_file))
    input_file.seek(0)
    dump(run_process(input_file, True))