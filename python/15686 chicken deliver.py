import itertools

N, M = map(int, input().split())
home = []
chicken = []
distances = []

for i in range(N):
    m = list(map(int, input().split()))
    for idx, n in enumerate(m):
        if n == 1:
            home.append((i, idx))
        elif n == 2:
            chicken.append((i, idx))

def distance(h, c):
    return abs(h[0] - c[0]) + abs(h[1] - c[1])


for idx, h in enumerate(home):
    distances.append(dict())
    for c in chicken:
        distances[idx][c] = distance(h, c)

cases = list(itertools.combinations(chicken, M))

def case_sum(case):
    dist_sum = 0
    for h in range(len(home)):
        dist_sum += min(distances[h][i] for i in case)
    return dist_sum

ans = 99999999999
for case in cases:
    ans = min(case_sum(case), ans)

print(ans)