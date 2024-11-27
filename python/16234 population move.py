import math
N, L, R = map(int, input().split())

A = []

for i in range(N):
    A.append(list(map(int, input().split())))

movex = [1, -1, 0, 0]
movey =[0, 0, 1, -1]

union_map = [[0 for i in range(N)] for j in range(N)]

day = 0
union_sum = 0

def border_open(c1, c2) -> bool:
    if 0 <= c2[0] < N and 0 <= c2[1] < N:
        diff = abs(A[c1[0]][c1[1]] - A[c2[0]][c2[1]])
        if L <= diff <= R:
            return True
    return False

def print_map():
    for i in range(N):
        for j in range(N):
            print(A[i][j], end=" ")
        print()

queue = [] # queue for bfs
union = set() #set to check union and check
updated = True
while updated:
    updated = False
    for i in range(N):
        for j in range(N):  # go for bfs
            if not union_map[i][j] == day: # if not searched before
                continue
            queue.append((i, j))
            union_map[i][j] += 1

            while queue:
                point = queue.pop()
                union.add(point)
                union_sum += A[point[0]][point[1]]

                for k in range(4):
                    neighbor = (point[0] + movex[k], point[1] + movey[k])
                    if border_open(point, neighbor) and union_map[neighbor[0]][neighbor[1]] == day:
                        queue.append(neighbor)
                        updated = True
                        union_map[neighbor[0]][neighbor[1]] += 1

            avg = math.floor(union_sum / len(union))
            while union:
                member = union.pop()
                A[member[0]][member[1]] = avg
            union_sum = 0

    if updated:
        day+=1
# print_map()
print(day)