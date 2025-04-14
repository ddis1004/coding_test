R, C, T = map(int, input().split())
room = []
purifier = []


for i in range(R):
    row = list(map(int, input().split()))
    for j in range(C):
        if row[j] == -1:
            purifier.append((i,j))
    room.append(row)


dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def spread(): 
    global room
    new_board = [[0 for j in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C): 
            if room[i][j] == -1:
                new_board[i][j] = -1
            elif room[i][j] > 0:
                new_board[i][j] += room[i][j]
                available_direction = 0
                for k in range(4):
                    new_x, new_y = i + dx[k], j + dy[k]
                    if 0 <= new_x < R and 0 <= new_y < C:
                        if not room[new_x][new_y] == -1:
                            available_direction += 1
                            new_board[new_x][new_y] += int(room[i][j]/5)
                # print(f'found dust: {(i, j)}, spreading in {available_direction} directions')
                new_board[i][j] -= int(room[i][j]/5) * available_direction
    room = new_board
    
def purify():
    # 위쪽 공기청정기 (반시계)
    upper = purifier[0][0]

    # 아래에서 위로 이동
    for i in range(upper - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    # 왼쪽에서 오른쪽으로 이동
    for i in range(C - 1):
        room[0][i] = room[0][i + 1]
    # 위에서 아래로 이동
    for i in range(upper):
        room[i][C - 1] = room[i + 1][C - 1]
    # 오른쪽에서 왼쪽으로 이동
    for i in range(C - 1, 1, -1):
        room[upper][i] = room[upper][i - 1]
    room[upper][1] = 0  # 정화기 옆칸은 0

    # 아래쪽 공기청정기 (시계 방향)
    lower = purifier[1][0]

    # 위에서 아래로 이동
    for i in range(lower + 1, R - 1):
        room[i][0] = room[i + 1][0]
    # 왼쪽에서 오른쪽으로 이동
    for i in range(C - 1):
        room[R - 1][i] = room[R - 1][i + 1]
    # 아래에서 위로 이동
    for i in range(R - 1, lower, -1):
        room[i][C - 1] = room[i - 1][C - 1]
    # 오른쪽에서 왼쪽으로 이동
    for i in range(C - 1, 1, -1):
        room[lower][i] = room[lower][i - 1]
    room[lower][1] = 0  # 정화기 옆칸은 0


def dust_sum():
    summ = 0
    for i in range(R):
        for j in range(C):
            if not room[i][j] == -1: 
                summ += room[i][j]
    return summ
for i in range(T):
    spread()
    purify()
print(dust_sum())