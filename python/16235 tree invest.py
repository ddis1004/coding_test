from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 초기 양분
field = [[5] * N for _ in range(N)]

# 각 셀마다 나무 나이를 저장 (정렬된 deque)
trees = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x - 1][y - 1].append(age)

# 8방향
directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

for _ in range(K):
    # 봄 & 여름
    new_trees = [[deque() for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                dead_nutrient = 0
                temp = deque()
                while trees[i][j]:
                    age = trees[i][j].popleft()
                    if field[i][j] >= age:
                        field[i][j] -= age
                        temp.append(age + 1)
                    else:
                        dead_nutrient += age // 2
                field[i][j] += dead_nutrient
                trees[i][j] = temp

    # 가을
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].appendleft(1)  # 어린 나무는 앞에 추가

    # 겨울
    for i in range(N):
        for j in range(N):
            field[i][j] += A[i][j]

# 전체 나무 개수 세기
result = 0
for i in range(N):
    for j in range(N):
        result += len(trees[i][j])
print(result)
