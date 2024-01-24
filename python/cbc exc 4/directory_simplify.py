input_string = (list(input().split('/')))
print(input_string)

def simplify(input_string):
    directory_stack = []
    for c in input_string:

        if c == '':
            continue
        elif c == '.':
            continue
        elif c == '..':
            if len(directory_stack) > 0:
                directory_stack.pop()
        else:
            directory_stack.append(c)
        print(directory_stack)
    return directory_stack

def print_directory(directory):
    for i in range(len(directory)):
        print('/', end ="")
        print(directory[i], end ="")
    print('/', end="")
    print(directory[-1])

a = simplify(input_string)
print_directory(a)