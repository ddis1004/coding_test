from collections import deque

N = int(input())
board = []

shark= [-1, -1]
shark_size = 2
grow_progression = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 9:
            shark[0] = i
            shark[1] = j
            row[j] = 0  # 상어 위치는 0으로 바꿔줌
    board.append(row)



def bfs(shark, board): 
    queue = deque()
    queue.append((shark[0], shark[1], 0))
    went = [[False for _ in range(N)] for _ in range(N)]
    candidate = []
    min_time = 100
    global shark_size, grow_progression
    while(queue):
        ## check here
        x, y, time = queue.popleft()
        if went[x][y] == True:
            continue
        went[x][y] = True
        #found prey
        if 0 < board[x][y] < shark_size:
            # print(x, y, min_time, time)
            # if time > min_time:
            #     continue
            # min_time = time
            candidate.append((x, y, time))
            
        ## add adjacent area
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N and not went[new_x][new_y]:
                if board[new_x][new_y] <= shark_size:
                    queue.append((new_x, new_y, time + 1))

        # compare candidates
    if candidate:
        # print(candidate)
        candidate = sorted(candidate, key=lambda pos: (pos[2], pos[0], pos[1]))
        x,y,t = candidate[0]
        shark[0] = x
        shark[1] = y
        board[x][y] = 0
        # print(f"went to {(x, y)}")

        grow_progression += 1
        if grow_progression == shark_size:
            grow_progression = 0
            shark_size += 1
        return t
    else:
        return -1


answ = 0            
while(True):
    time = bfs(shark, board)
    if(time > 0):
        answ += time
    else:
        print(answ)
        # print(board)
        break
