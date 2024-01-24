
shortcut_count, destination = map(int, input().split())

shortcut_list = []
for i in range(shortcut_count):
    input_list = list(map(int, input().split()))
    sc = {"start":input_list[0], "end":input_list[1], "length" : input_list[2]}
    shortcut_list.append(sc)

shortcut_list = sorted(shortcut_list, key=lambda shortcut:(shortcut["start"]))

route_queue = []
# route {current, shortcut_plan(-1 if not taking shortcut), distance_so_far}
min_distance = destination

def go_straight_crossroad(x):
    crossroad = -1
    answ =[]
    for sc in shortcut_list:
        if sc['start'] > x:
            crossroad = sc['start']
            break
    for idx, sc in enumerate(shortcut_list):
        if sc['start'] == crossroad:
            answ.append(idx)
    return answ

def is_crossroad(x):
    for sc in shortcut_list:
        if sc['start'] == x:
            return True
    return False

def get_this_crossroad(x):
    i = 0
    answ = []
    for sc in shortcut_list:
        if sc['start'] == x:
            answ.append(i)
        i+=1
    return answ

def letsgo():
    route = route_queue.pop(0)
    current = route['current']
    distance_so_far = route['distance_so_far']

    if current == destination:
        global min_distance
        if min_distance > distance_so_far:
            min_distance = distance_so_far
            return


    if route['shortcut'] == -1:  # just taking the normal route
        crossroad = go_straight_crossroad(current)
        if len(crossroad) == 0: # direct to destination
            if current <= destination:
                total_distance = distance_so_far + destination - current
                if min_distance > total_distance:
                    min_distance = total_distance
            return

        distance_so_far += shortcut_list[crossroad[0]]['start'] - current
        current = shortcut_list[crossroad[0]]['start']

        # move to the crossroad, insert all possibility in queue
        route_queue.append({'current': current, 'shortcut': -1, 'distance_so_far': distance_so_far})
        for i in crossroad:
            route_queue.append({'current': current, 'shortcut': i, 'distance_so_far': distance_so_far})

    else:
        distance_so_far += shortcut_list[route['shortcut']]['length']
        current = shortcut_list[route['shortcut']]['end']

        if is_crossroad(current): #this spot is crossroad
            crossroad = get_this_crossroad(current)
            route_queue.append({'current': current, 'shortcut': -1, 'distance_so_far': distance_so_far})
            for i in crossroad:
                route_queue.append({'current': current, 'shortcut': i, 'distance_so_far': distance_so_far})
        else: #lets move to next crossroad
            route_queue.append({'current': current, 'shortcut': -1, 'distance_so_far': distance_so_far})

        return



route_queue.append({'current': 0, 'distance_so_far': 0, 'shortcut': -1})
for idx, sc in enumerate(shortcut_list):
    if sc['start'] == 0:
        route_queue.append({'current': 0, 'distance_so_far': 0, 'shortcut': idx})


while len(route_queue) > 0:
     letsgo()

print(min_distance)

