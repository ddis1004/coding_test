m, n = map(int, input().split())

input_list = list(map(int, input().split()))
queen_loc = [input_list[x:x + 2] for x in range(1, len(input_list), 2)]
input_list = list(map(int, input().split()))
knight_loc = [input_list[x:x + 2] for x in range(1, len(input_list), 2)]
input_list = list(map(int, input().split()))
pawn_loc = [input_list[x:x + 2] for x in range(1, len(input_list), 2)]
del input_list

board = [[0 for j in range(n)] for i in range(m)]
checklist = [[0 for j in range(n)] for i in range(m)]

knight_moves = [[2, 1], [1, 2], [2, -1], [-1, 2], [-2, 1], [1, -2], [-2, -1], [-1, -2]]
queen_moves = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]


def in_board(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    else:
        return True


def is_obstacle(x, y):
    c = board[x][y]
    if c == 'p' or c == 'q' or c == 'k':
        return True
    else:
        return False


def knight_check(kloc):
    for km in knight_moves:
        x = kloc[0] - 1 + km[0]
        y = kloc[1] - 1 + km[1]
        if in_board(x, y) and is_obstacle(x, y) == False:
            if board[x][y] == 0:
                board[x][y] = -1


def queen_check(qloc):
    for qm in queen_moves:
        checklist[qloc[0] - 1][qloc[1] - 1] = 1
        distance = 1
        x = qloc[0] - 1 + qm[0] * distance
        y = qloc[1] - 1 + qm[1] * distance
        while in_board(x, y) and is_obstacle(x, y) == False:
            board[x][y] = -1
            distance += 1
            x = qloc[0] - 1 + qm[0] * distance
            y = qloc[1] - 1 + qm[1] * distance

def visualize_board():
    for i in range(m):
        for j in range(n):
            print(board[i][j], end="\t")
        print()


for qloc in queen_loc:
    board[qloc[0] - 1][qloc[1] - 1] = 'q'
for kloc in knight_loc:
    board[kloc[0] - 1][kloc[1] - 1] = 'k'
for ploc in pawn_loc:
    board[ploc[0] - 1][ploc[1] - 1] = 'p'

for qloc in queen_loc:
    queen_check(qloc)
for kloc in knight_loc:
    knight_check(kloc)

#visualize_board()

answ = 0
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            answ += 1

print(answ)
