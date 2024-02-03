import collections

N, M, T = map(int, input().split())

def floyd_warshall(distances):
    for i in range(N + 1):
        distances[i][i] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                distances[i][j] = min(distances[i][j], max(distances[i][k], distances[k][j]))
    return distances


distances = [[float('inf') for i in range(N + 1)] for j in range(N + 1)]

for i in range(M):
    s, e, h = map(int, input().split())
    distances[s][e] = h

floyd_warshall(distances)

answers = []
for i in range(T):
    s, e = map(int, input().split())
    answers.append(distances[s][e])

for answ in answers:
    if answ <= 1000000:
        print(answ)
    else:
        print(-1)