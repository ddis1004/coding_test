N, K = map(int, input().split())

belt = list(map(int, input().split()))
load_point = 0
unload_point = N - 1
belt_length = 2 * N
broke_count = 0  
time = 1
bots = []

def bot_move(b, i) : 
    next_point = (b + 1) % belt_length
    global broke_count
    if next_point == unload_point:
        belt[next_point] -= 1
        bots.pop(i)
    else: 
        bots[i] = next_point
        belt[next_point] -= 1

    if belt[next_point] == 0:
        broke_count += 1


while True:
    #belt spin
    unload_point = (unload_point - 1) % belt_length
    load_point = (load_point - 1) % belt_length

    # unload bot on point immediately
    if bots and bots[0] == unload_point:
        bots.pop(0)

    # if front bot will reach the end
    if bots and bots[0] == (unload_point - 1) % belt_length:
        # check durability
        if belt[unload_point] > 0:
            belt[unload_point] -= 1
            bots.pop(0)
            if belt[unload_point] == 0:
                broke_count += 1

    #bot moves
    for i, b in enumerate(bots):
        next_point = (b + 1) % belt_length
        # if front empty
        if i == 0 or bots[i - 1] != next_point: 
            # if front durability ok
            if belt[next_point] > 0:
                #move bot
                bots[i] = next_point
                belt[next_point] -= 1
                if belt[next_point] == 0:
                    broke_count += 1    

    #load, decrease durability
    if belt[load_point] > 0:
        bots.append(load_point)
        belt[load_point] -= 1
        if belt[load_point] == 0:
            broke_count += 1
    
    if broke_count >= K:
        print(time)
        break

    time += 1



