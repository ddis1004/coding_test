from collections import deque

N, M, T = map(int, input().split())

map = [(list(map(int, input().split()))) for _ in range(N)]
visited = [[False for i in range(M)] for i in range(N)]

queue = deque()
queue.append(((0, 0), 0, False))  # (position, time, sword)
directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def bfs():
    min_time = float('inf')
    while queue:
        position, time, sword = queue.popleft()
        if time >= min_time:
            return min_time
        if time >= T and min_time >= T:
            return -1
        for direction in directions:
            x, y = position[0] + direction[0],  position[1] + direction[1]
            if 0 <= x < N and 0 <= y < M and map[x][y] != 1:
                if not visited[x][y]:
                    visited[x][y] = True
                    if x == N - 1 and y == M - 1:
                        min_time = min(min_time, time + 1)
                    if map[x][y] == 0:
                        queue.append(((x, y), time + 1, sword))
                    elif map[x][y] == 2:
                        sword_time = time + (N - 1 - x) + (M - 1 - y) + 1
                        if sword_time <= T:
                            min_time = min(min_time, sword_time)

    if min_time <= 100000:
        return min_time
    else:
        return -1

answ = bfs()
if answ < 0:
    print("Fail")
else:
    print(answ)

