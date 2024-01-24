N, M = map(int, input().split())

board = []
check_board = [[True for i in range(M)] for j in range(N)]

for i in range(N):
    board.append(list(input().split()))

word = input()


def search(word):

    def in_board(coord):
        if coord[0] >=0 and coord[0] < N:
            if coord[1] >=0 and coord[1] < M:
                return True
        return False

    def dfs(x, y, depth):
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        if depth == len(word) - 1:
            return True
        check_board[x][y] = False
        for direct in directions:
            coord_to_check = (x + direct[0], y + direct[1])
            if in_board(coord_to_check) and check_board[coord_to_check[0]][coord_to_check[1]]:
                if board[coord_to_check[0]][coord_to_check[1]] == word[depth + 1]:
                    #print('coord to check : ', coord_to_check, 'word til now', word[:depth], 'depth: ', depth)
                    return dfs(coord_to_check[0], coord_to_check[1], depth + 1)
        check_board[x][y] = True
        return False


    for i in range(N):
        for j in range(M):
            if board[i][j] == word[0]:
                if dfs(i,j,0):
                    return True
    return False

print(search(word))