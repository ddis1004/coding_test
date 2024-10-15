import collections
N = int(input())
TP = []
for i in range(N):
    (T, P) = map(int, input().split())
    TP.append((T, P))

dynamic_max = collections.defaultdict(int)
max_max = collections.defaultdict(int)
answer = 0

for i in range(N-1, -1, -1):
    (T, P) = TP[i]
    if i + T - 1 > N - 1:
        dynamic_max[i] = 0
        max_max[i] = max(max_max[i + 1], dynamic_max[i])
    else:
        dynamic_max[i] = max_max[i + T] + P
        max_max[i] = max(max_max[i + 1], dynamic_max[i])

    answer = max(max_max[i], answer)

print(answer)
