N, M, y, x, K = map(int, input().split())
field = []
for i in range(N):
    field.append(list(map(int, input().split())))
moves = list(map(int, input().split()))

sides = [0, 0, 0, 0, 0, 0]

direction = [(0, 0), (0,  1), (0, -1), (-1, 0), (1, 0)]

def in_field(a, b):
    if 0 <= a < M and 0 <= b < N:
        return True
    return False

for m in moves:
    # print(y, x)
    if not in_field(x + direction[m][1], y + direction[m][0]):
        continue
    x, y = (x + direction[m][1], y + direction[m][0])

    if m == 1:
        sides = [sides[3], sides[1], sides[0], sides[5], sides[4], sides[2]]
    elif m == 2:
        sides = [sides[2], sides[1], sides[5], sides[0], sides[4], sides[3]]
    elif m == 3:
        sides = [sides[4], sides[0], sides[2], sides[3], sides[5], sides[1]]
    elif m == 4:
        sides = [sides[1], sides[5], sides[2], sides[3], sides[0], sides[4]]

    if field[y][x] == 0:
        field[y][x] = sides[5]
    else:
        sides[5] = field[y][x]
        field[y][x] = 0


    print(sides[0])
