import itertools as iter
N, M = map(int, input().split())
lab = []
virus = []
blank_count = 0
for i in range(N):
    frag = list(map(int, input().split()))
    for j in range(M):
        if frag[j] == 2:
            virus.append((i, j))
        elif frag[j] == 0:
            blank_count += 1
    lab.append(frag)


def in_board(point):
    if 0 <= point[0] < N:
        if 0 <= point[1] < M:
            return True
    return False

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
import copy

def bfs(start_points, new_wall, stop_area):
    queue = copy.deepcopy(start_points)
    traversed = set(start_points)
    area = 0
    while len(queue) > 0 and area < stop_area:
        point = queue.pop()
        area += 1
        for d in directions:
            new_point = (point[0] + d[0], point[1] + d[1])
            if in_board(new_point) and lab[new_point[0]][new_point[1]] == 0:
                if new_point not in traversed and new_point not in new_wall:
                    traversed.add(new_point)
                    queue.append(new_point)

    return area

possibilities = iter.combinations(range(N * M), 3)
answer = N * M  + 100
for p in possibilities:
    walls = []
    for j in p:
        x, y = j // M, j % M
        if lab[x][y] == 0:
            walls.append((x, y))
    if len(walls) == 3:
        answer = min(answer, bfs(virus, walls, answer))
    walls.clear()

print(blank_count - answer - 3 + len(virus))


# for p in possibilities:
#     print('[', end = '')
#     for j in p:
#         print("(", end = "")
#         print(j // N, ", " , j % M, end ="")
#         print(")", end="")
#     print(']', end = '\n')
