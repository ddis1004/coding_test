N = int(input())
str_list = []
for i in range(N):
    str_list.append(list(input()))

def is_VPS(str):
    stack = []
    for c in str:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not len(stack) == 0:
                stack.pop()
            else:
                return 'NO'
        else:
            return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


for str in str_list:
    print(is_VPS(str))