string = list(input())
#print(string)

cursor = len(string) - 1
count = 0

while cursor >= 0:
    c = string[cursor]

    if c == '=':
        #print(f'found letter is = ', end = '')
        prev_c = string[cursor - 1]
        if prev_c == 's' or prev_c == 'c':
            #print(f'prev letter is {prev_c}')
            cursor = cursor - 2
        elif prev_c == 'z':
            if cursor - 1 > 0 :
                if string[cursor - 2] == 'd':
                    #print(f'prev letter is {prev_c}, prev_prev is {string[cursor - 2]}')
                    cursor -= 3
                else:
                    #print(f'prev letter is {prev_c}, prev_prev is {string[cursor - 2]} so just moving on')
                    cursor -=2
            else:
                #print(f'prev letter is {prev_c} that was the last letter')
                cursor -=2
        else:
            #print(f'Unexpected character found at index[{cursor-1}]')
            break
    elif c == '-':
        prev_c = string[cursor - 1]
        if prev_c == 'c' or prev_c == 'd':
            cursor -= 2
    elif c == 'j':
        prev_c = string[cursor - 1]
        if prev_c == 'l' or prev_c =='n':
            cursor -= 2
        else:
            cursor -=1
    else:
        cursor -=1

    count +=1

print(count)