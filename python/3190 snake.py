from collections import deque

N = int(input())
K = int(input())

apples = []

for i in range(K):
    (x, y) = map(int, input().split())
    apples.append((x - 1, y - 1))

L = int(input())

route = []
for i in range(L):
    X, C = input().split()
    route.append((int(X), C))

time = 0

snake = deque()
snake.append((0, 0))
direction = 0

def move_head(current_head, dir):
    if dir == 0:
        return (current_head[0], current_head[1] + 1)
    elif dir == 1:
        return (current_head[0] + 1, current_head[1])
    elif dir == 2:
        return (current_head[0], current_head[1] - 1)
    elif dir == 3:
        return (current_head[0] - 1, current_head[1])

def dead(head):
    if head in snake:
        return True
    if head[0] < 0 or head[0] >= N or head[1] < 0 or head[1] >= N:
        return True
    return False

while True:
    # print(snake[0])
    if len(route) > 0 and time == route[0][0]:
        # update direction
        if route[0][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        route.pop(0)
    time += 1
    next_head = move_head(snake[0], direction)
    if dead(next_head):
        break
    snake.appendleft(next_head)
    if next_head in apples:
        apples.remove(next_head)
    else:
        snake.pop()

print(time)






