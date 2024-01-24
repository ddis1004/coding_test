N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))


def next_size(size, array, direction):
    print(f'size : {size}, direction:{direction}')
    answer = []
    #first go with x-side expand
    if direction == 'x':
        for coord in array:
            if coord[0] + size[0] >= N: # at the end of the board
                continue
            if 0 in board[coord[0] + size[0]][coord[1]: coord[1] + size[1]]:
                continue
            #print(board[coord[0] + size[0]][coord[1]: coord[1] + size[1]])
            answer.append(coord)

    if direction == 'y':
        for coord in array:
            if coord[1] + size[1] >= M: # at the end of the board
                continue
            #print(board[coord[0]: coord[0] + size[0]])
            answer.append(coord)
            for i in range(coord[0], coord[0] + size[0], 1):
                if board[i][coord[1] + size[1]] == 0:
                    answer.pop()
                    break

    print(answer)
    return answer

zerozero = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            zerozero.append((i,j))


def do_it(xsize, ysize, array):
    xexpanded = next_size((xsize,ysize), array, 'x')
    if xexpanded:
        size2 = do_it(xsize + 1, ysize, xexpanded)
    yexpanded = next_size((xsize,ysize), array, 'y')
    if yexpanded:
        size1 = do_it(xsize, ysize + 1, yexpanded)

    if not xexpanded and not yexpanded:
        return 0
    elif not xexpanded:
        return (xsize) * (ysize + 1)
    elif not yexpanded:
        return (ysize + 1) * (ysize)
    else:
        #print(f'returning {max((xsize + 1) * (ysize), (xsize) * (ysize + 1))}')
        return max(size1, size2)

print(do_it(1, 1, zerozero))