def solution(bridge_length, weight, truck_weights):
    bridge_queue = [0 for i in range(bridge_length)]
    time = 0

    def weight_on_bridge(bridge_queue):
        ans = 0
        for b in bridge_queue:
            ans += b
        return b

    while len(truck_weights) > 0:
        time += 1
        if weight_on_bridge(bridge_queue) + truck_weights[-1] <= weight:
            bridge_queue.append(truck_weights.pop(0))
        else:
            bridge_queue.append(0)
        bridge_queue.pop(0)
        print(bridge_queue)

    return time


print(solution(2, 10, [7,4,5,6]))