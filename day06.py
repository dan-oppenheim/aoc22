
def find_marker(input_file, length):
    code = []
    for i, c in enumerate(input_file.read()):
        if c not in code:
            code.append(c)
            if len(code) == length:
                return i+1
        else:
            code = code[code.index(c)+1:]
            code.append(c)

with open("input/day6.txt") as input_file:
    print(find_marker(input_file, 4))
    input_file.seek(0)
    print(find_marker(input_file, 14))