N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def traversable(road: list) -> bool:
    i = 1
    height_streak = 1
    prev_height = road[0]
    
    while i < N:
        if prev_height == road[i]:
            height_streak += 1
            i += 1
        elif prev_height + 1 == road[i]:
            if height_streak >= L:
                height_streak = 1
                prev_height += 1
                i += 1
            else:
                return False
        elif prev_height - 1 == road[i]:
            for _ in range(L - 1):
                i += 1
                if i >= N or road[i] != prev_height - 1:
                    return False
            prev_height = prev_height - 1
            height_streak = 0
            i += 1
        else:
            return False
    return True

answ = 0

#starting from horizontal
for i in range(N):
    road = arr[i]
    if traversable(road):
        answ += 1
        # print('hor', i)

#next vertical
for i in range (N):
    road = [arr[j][i] for j in range(N)]
    if traversable(road):
        answ += 1
        # print('ver', i)

print(answ)
