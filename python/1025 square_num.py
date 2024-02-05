#handling input
import collections

N, M = map(int, input().split())
table = []
for i in range(N):
    row = list(map(int, input()))
    table.append(row)

#initialize square set to check if a number is a square number
squares = set()
n = 0
while n * n <= 10 ** (max(N, M) + 1):
    squares.add(n * n)
    n += 1

#return largest square number with given difference
def exploreMap(difference : tuple) -> int:
    max_square = -1
    #try starting from all positions
    for i in range(N):
        for j in range(M):
            numbers = getNumber((i,j), difference)
            #if found number is square
            for n in numbers:
                if n in squares:
                    max_square = max(max_square, n)
    return max_square


#return numbers at given start_point and difference
def getNumber(start_point: tuple, difference: tuple) -> list:
    x, y = start_point
    i, j = difference
    sequence = []
    sequence.append(table[x][y])
    numbers = []
    numbers.append(int(''.join(map(str, sequence))))

    while x + i >= 0 and x + i < N and y + j >= 0 and y + j < M:
        x += i
        y += j
        sequence.append(table[x][y])
        numbers.append(int(''.join(map(str, sequence))))
    return numbers

# bfs the difference and its biggest square_num
def bfs():
    max_square = -1
    queue = collections.deque()
    explored = set()
    queue.append((1, 0))
    queue.append((0, 1))
    queue.append((1, 1))
    queue.append((-1, 0))
    queue.append((0, -1))
    queue.append((-1, -1))

    explored.add((0, 0))
    explored.add((1, 0))
    explored.add((0, 1))
    explored.add((1, 1))
    explored.add((-1, 0))
    explored.add((0, -1))
    explored.add((-1, -1))

    while queue:
        i, j = queue.popleft()
        max_square = max(max_square, exploreMap((i, j)))
        if i + 1 <= N - 1 and (i + 1, j) not in explored:
            queue.append((i + 1, j))
            explored.add((i + 1, j))
        if j + 1 <= M - 1 and (i, j + 1) not in explored:
            queue.append((i, j + 1))
            explored.add((i, j + 1))
        if j + 1 <= M - 1 and i + 1 <= N - 1 and (i + 1, j + 1) not in explored:
            queue.append((i + 1, j + 1))
            explored.add((i + 1, j + 1))
        if i - 1 > -N and (i - 1, j) not in explored:
            queue.append((i - 1, j))
            explored.add((i - 1, j))
        if j - 1 > -M and (i, j - 1) not in explored:
            queue.append((i, j - 1))
            explored.add((i, j - 1))
        if i - 1 > -N and j - 1 >= -M and (i - 1, j - 1) not in explored:
            queue.append((i - 1, j - 1))
            explored.add((i - 1, j - 1))
    return max_square

print(bfs())