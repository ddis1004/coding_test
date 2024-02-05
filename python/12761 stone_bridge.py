from collections import deque

A, B, N, M = map(int, input().split())

queue = deque()
queue.append((N, 0))  # (position, moves)


def bfs(queue):
    visited = set()

    while len(queue) > 0:
        position, moves = queue.popleft()
        if position == M:
            return moves
        if position + 1 <= 100000 and position + 1 not in visited:
            queue.append((position + 1, moves + 1))
            visited.add(position + 1)
        if position - 1 >= 0 and position - 1 not in visited:
            queue.append((position - 1, moves + 1))
            visited.add(position - 1)
        if position + A <= 100000 and position + A not in visited:
            queue.append((position + A, moves + 1))
            visited.add(position + A)
        if position + B <= 100000 and position + B not in visited:
            queue.append((position + B, moves + 1))
            visited.add(position + B)
        if position - A >= 0 and position - A not in visited:
            queue.append((position - A, moves + 1))
            visited.add(position - A)
        if position - B >= 0 and position - B not in visited:
            queue.append((position - B, moves + 1))
            visited.add(position - B)
        if position * A <= 100000 and position * A not in visited:
            queue.append((position * A, moves + 1))
            visited.add(position * A)
        if position * B <= 100000 and position * B not in visited:
            queue.append((position * B, moves + 1))
            visited.add(position * B)


print(bfs(queue))