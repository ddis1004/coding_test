T = list(map(int, input().split()))

def warmer_day(T):
    stack = []
    answer = [0 for i in range(len(T))]
    for i in range(len(T)):
        if len(stack) == 0 or T[i] < stack[-1][0]:
            #print('colder day')
            #print(stack)
            stack.append((T[i], i))
        else:
            while len(stack) > 0 and T[i] > stack[-1][0]:
                #print('warmer day')
                s = stack.pop()
                answer[s[1]] = i - s[1]
            stack.append((T[i], i))
    return answer

print(warmer_day(T))



