route1 = [[1,2,7], [3,6,7]]

def bfs(route, start, destination):

    stack = []
    went = [start]
    if start == destination:
        return 0

    for r in route:
        if start in r:
            for stop in r:
                if stop is not start:
                    stack.append({'depth': 1, 'node': stop})

    while stack :
        print(stack)
        ah = stack.pop(0)
        for r in route:
            if ah['node'] in r:
                for stop in r:
                    if stop == 6:
                        return ah['depth'] + 1
                    if stop is not start and stop not in went:
                        stack.append({'depth': ah['depth'] + 1, 'node': stop})
                        went.append(stop)


print(bfs(route1, 1, 6))