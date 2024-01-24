N = int(input())
ground = list(map(int, input().split()))

max_height = max(ground)

def water_at_height(h):
    #print(f'height : {h}')
    answ = 0
    start = -1
    end = -1

    for i in range(N): #find first ground at the height
        if ground[i] >= h:
            #print(f'found first ground at {i}')
            start = i
            end = i
            break

    for i in range(start, N, 1):
        end += 1
        if ground[end] >= h:
            #print(f'start: {start}, end: {end}, water_amount: {end - start - 1}')
            answ += end - start - 1
            start = end
    #print(f'returning {answ}')
    #print()
    return answ




answ = 0
for i in range(max_height, 0 , -1):
    answ += water_at_height(i)

print(answ)
