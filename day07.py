class File:
    def __init__(self, name:str, size:int):
        self.name:str = name
        self.size:int = size

    def __str__(self):
        return f"{self.name} {self.size}"

class Directory:
    def __init__(self, name:str, parent:'Directory'):
        self.name:str = name
        self.parent:Directory = parent
        self.children:dict[str, File|Directory] = {}

    def __str__(self):
        return f"{self.name}" + '\n\t'.join([str(v) for v in self.children.values()])

class Context:
    def __init__(self, root:Directory):
        self.root:Directory = root
        self.cwd:Directory = root

    def __str__(self):
        return str(self.root)


def print_fs(directory:Directory, depth:int):
    print("\t" * depth + directory.name + "(dir)")
    depth += 1
    for v in directory.children.values():
        if isinstance(v, File):
            print("\t" * depth + str(v))
        else:
            print_fs(v, depth)

def get_size(sizes:dict[str, int], children:list[Directory|File], path:list[str]):
    size = 0
    if len(children) == 0:
        print("no children")
    for child in children:
        if isinstance(child, File):
            size += child.size
        else:
            path.append(child.name)
            dir_size = get_size(sizes, child.children.values(), path)
            sizes[path[0] + '/'.join(path[1:])] = dir_size
            size += dir_size
            path.pop()
    return size

def get_dir_sizes(ctx:Context):
    sizes:dict[str,int] = {}
    sizes['/'] = get_size(sizes, ctx.root.children.values(), ['/'])
    return sizes

def get_sum_of_dir_under(sizes:dict[str,int], size):
    for k, v, in sizes.items():
        print(k, v)
        
    sum = 0
    for v in sizes.values():
        if v <= size:
           sum += v
    return sum 

def get_used_size(sizes:dict[str, int]):
    return sizes['/']

def get_smallest_to_achieve_free_space(sizes:dict[str, int], min_size):
    return [size for size in sorted(sizes.values()) if size > min_size][0]

def handle_cmd(ctx:Context, cmd:list[str]):
    if cmd[0] == 'cd':
        if cmd[1] == '..':
            ctx.cwd = ctx.cwd.parent
        elif cmd[1] == '/':
            ctx.cwd = ctx.root
        else:
            ctx.cwd = ctx.cwd.children[cmd[1]]
    elif cmd[0] == 'ls':
        pass   

def main():
    with open('input/day7.txt') as input_file:
        ctx = Context(Directory("/", None))
        num_dirs = 1
        for line in input_file:
            if line[0] == '$':
                handle_cmd(ctx, line.split()[1:])                
            else:
                parts = line.split()
                if parts[0] == 'dir':
                    num_dirs += 1
                    ctx.cwd.children[parts[1]] = Directory(parts[1], ctx.cwd)
                else:
                    ctx.cwd.children[parts[1]] = File(parts[1], int(parts[0]))
        #print_fs(ctx.root, 0)
        sizes = get_dir_sizes(ctx)
        print(get_sum_of_dir_under(sizes, 100000))
        print(get_smallest_to_achieve_free_space(sizes, 30000000-(70000000-get_used_size(sizes))))
main()