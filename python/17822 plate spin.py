from collections import deque
N, M, T = map(int, input().split())
plates = [list(map(int, input().split())) for i in range(N)]
plate_spin = [0 for i in range(N)]
spins = [list(map(int, input().split())) for i in range(T)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def adjacent(i, j):
    # 회전상황을 고려해서 인접한 숫자를 노드에 추가해야함.
    adjacent = []
    adjacent.append((i, (j - 1) % M))
    adjacent.append((i, (j + 1) % M))
    if i - 1 >= 0:
        adjacent.append((i - 1, (j + (plate_spin[i] - plate_spin[i - 1])) % M))
    if i + 1 < N:
        adjacent.append((i + 1, (j + (plate_spin[i] - plate_spin[i + 1])) % M))
    return adjacent

def erase_same(start):
    start_x, start_y = start
    number = plates[start_x][start_y]
    count = 0
    
    # check start-adjacent area 
    for point in adjacent(start_x, start_y):
        if number == plates[point[0]][point[1]]:
            count += 1
    
    # if same number exist, go for bfs
    
    if count > 0:
        #bfs
        went = [[False for j in range(M)] for i in range(N)]
        queue = deque()
        queue.append((start_x, start_y))
        while queue:
            i, j = queue.popleft()
            # have to erase same num
            plates[i][j] = -1
            for point in adjacent(i, j):
                if number == plates[point[0]][point[1]]:
                    if not went[point[0]][point[1]]:
                        went[point[0]][point[1]] = True
                        queue.append((point[0], point[1]))
        return True
    return False
    

    

for spin in spins:
    x, d, k = spin
    for i in range(x, N + 1, x):  # x의 배수 spin
        if d == 0:  # clockwise
            plate_spin[i - 1] = (plate_spin[i - 1] + k) % M
        if d == 1:  # counter-clockwise
            plate_spin[i - 1] = (plate_spin[i - 1] - k) % M

    has_erased = False
    visited = [[False] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if plates[i][j] != -1 and not visited[i][j]:
                erased = erase_same((i, j))
                if erased:
                    has_erased = True
                visited[i][j] = True  # 이미 erase_same에서 방문했으니 중복 호출 방지

    if not has_erased:
        total = 0
        count = 0
        for i in range(N):
            for j in range(M):
                if plates[i][j] != -1:
                    total += plates[i][j]
                    count += 1
        if count > 0:
            avg = total / count
            for i in range(N):
                for j in range(M):
                    if plates[i][j] != -1:
                        if plates[i][j] > avg:
                            plates[i][j] -= 1
                        elif plates[i][j] < avg:
                            plates[i][j] += 1

answ = 0
for i in range(N):
    for j in range(M):
        if not plates[i][j] == -1:
            answ += plates[i][j]
print(answ)