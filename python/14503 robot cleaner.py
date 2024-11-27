N, M = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))
room = []

for i in range(N):
    room.append(list(map(int, input().split())))

def around_uncleaned(x, y):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        # if 0 <= x + move[0] < N and 0 <= y + move[1] < M:  # end of room is wall
        if room[x + move[0]][y + move[1]] == 0:
             return True
    return False


direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
clean_count = 0
while True:
    if room[r][c] == 0: #현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        room[r][c] = -1
        clean_count += 1

    if around_uncleaned(r, c):
        d = (d - 1) % 4 #반시계 방향으로 90도 회전한다
        if room[r + direction[d][0]][c + direction[d][1]] == 0: #바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            r = r + direction[d][0]
            c = c+ direction[d][1]

    else: #현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if room[r - direction[d][0]][c - direction[d][1]] == 1: #바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            break
        else: #바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            r = r - direction[d][0]
            c = c - direction[d][1]


print(clean_count)


