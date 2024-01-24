encoded_stack = list(input())
decoded= []
resolve_buffer = []

def decode():
    depth = 0
    global decoded
    while len(encoded_stack) > 0:
        c = encoded_stack.pop()
        #print(f'stack: {encoded_stack}')
        if depth == 0:
            if c == ']':
                #print('met [ moving to resolving stage')
                depth +=1
            else:
                #print(f'got {c} as input. depth = 0 so just inserting at decode stack')
                decoded.insert(0, c)
        else:
            #print(f'got {c} as input. depth != 0 trying to resolve []')
            if c == ']': # do nothing if [
                depth += 1
            elif c.isalpha():
                resolve_buffer.insert(0,c)
            elif c.isdigit():
                #print(resolve_buffer)
                for i in range(int(c)):
                    for j in resolve_buffer:
                        encoded_stack.append(j)
                # print(encoded_stack)
                while len(resolve_buffer) > 0: #resetting resolving buffer
                    resolve_buffer.pop()
                depth -= 1

decode()
for i in decoded:
    print(i, end="")





