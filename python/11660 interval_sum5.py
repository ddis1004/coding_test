N, M = map(int, input().split())

min_x, min_y, max_x, max_y = float('inf'), float('inf'), 0, 0

table = [list(map(int, input().split())) for _ in range(N)]

intervals = []

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = map(lambda x: x-1, (x1, y1, x2, y2))
    max_x = max(x2, max_x)
    max_y = max(y2, max_y)
    intervals.append((x1, y1, x2, y2))


def intervalSumTable(x_interval, y_interval):
    x1, x2 = x_interval
    y1, y2 = y_interval
    sumTable = [[0 for _ in range(y2 - y1 + 1)] for __ in range(x2 - x1 + 1)]

    for i in range(x2 - x1 + 1):
        for j in range(y2 - y1 + 1):
            if i == 0 and j == 0:
                sumTable[i][j] = table[x1 + i][y1 + j]
            elif j == 0:
                sumTable[i][j] = sumTable[i - 1][j] + table[x1 + i][y1 + j]
            elif i == 0:
                sumTable[i][j] = sumTable[i][j - 1] + table[x1 + i][y1 + j]
            else:
                sumTable[i][j] = sumTable[i][j - 1] + sumTable[i - 1][j] - sumTable[i - 1][j - 1] + table[x1 + i][y1 + j]


    return sumTable

sumTable = intervalSumTable((0, max_x), (0, max_y))


for interval in intervals:
    x1, y1, x2, y2 = interval
    k = sumTable[x2][y2]
    if x1 - 1 >= 0 and y1 - 1 >= 0:
        k += sumTable[x1 - 1][y1 - 1]
    if x1 - 1 >= 0:
        k -= sumTable[x1 - 1][y2]
    if y1 - 1 >= 0:
        k -= sumTable[x2][y1 - 1]

    #
    # if x1 == 0 or y1 == 0:
    #     k = sumTable[x2][y2]
    # else:
    #     k = sumTable[x2][y2] + sumTable[x1 - 1][y1 - 1] - sumTable[x2][y1 - 1] - sumTable[x1 - 1][y2]
    print(k)