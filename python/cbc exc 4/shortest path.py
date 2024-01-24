M, N = map(int, input().split())
board = []
dp = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    board.append(list(map(int, input().split())))


def shortest(board):
    dp[0][0] = board[0][0]
    for i in range(N):
        for j in range(M):
            if i == 0:
                dp[i][j] = dp[i][j-1] + board[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + board[i][j]
            else:
                dp[i][j] = board[i][j] + min(dp[i][j-1], dp[i-1][j])

    return dp[N-1][M-1]

print(shortest(board))