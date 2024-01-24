N, M = map(int, input().split())
world = []

for i in range(N):
    world.append(list(map(int, input().split())))

def in_world(x,y):
    if x < N and x >= 0 and y < M and y >= 0:
        return True
    return False

def bfs_wrap(world):
    queue = []
    island_count = 0

    def explore(x,y):
        world[x][y] = 0
        direction_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for d in direction_list:
            if in_world(x + d[0], y + d[1]) and world[x+d[0]][y+d[1]] == 1:
                queue.append([x + d[0], y + d[1]])


    for i in range(N):
        for j in range(M):
            if world[i][j] == 1:
                queue.append((i, j))
                island_count += 1
                while len(queue) > 0:
                    coord = queue.pop(0)
                    explore(coord[0], coord[1])

    return island_count

def dfs_wrap(world):

    stack = []
    island_count = 0

    def explore(x,y):
        direction_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        world[x][y] = 0
        for d in direction_list:
            if in_world(x + d[0], y + d[1]) and world[x + d[0]][y + d[1]] == 1:
                stack.insert(0, [x + d[0], y + d[1]])

    for i in range(N):
        for j in range(M):
            if world[i][j] == 1:
                print(f'found 1 at [{i},{j}]')
                stack.insert(0, [i,j])
                island_count += 1
                while len(stack) > 0:
                    print(stack)
                    coord = stack.pop(0)
                    explore(coord[0], coord[1])

    return island_count



#print(bfs_wrap(world))
print(dfs_wrap(world))