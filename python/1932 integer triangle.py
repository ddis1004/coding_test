size = int(input())
tower = [] #k번째 층 i번째 요소로 표현 예정
max_tower = []
for k in range(size):
    tower.append(list(map(int, input().split())))
    max_tower.append([0 for i in range(k+1)])

def calculate_floor(k):
    for i in range(k + 1):
        if i == 0: #when it is on left end
            max_tower[k][i] = tower[k][i] + max_tower[k - 1][0]
        elif i == k: #when it is on right end
            max_tower[k][i] = tower[k][i] + max_tower[k - 1][k-1]
        else:
            max_tower[k][i] = tower[k][i] + max(max_tower[k-1][i-1], max_tower[k-1][i])

max_tower[0][0] = tower[0][0]

for k in range(1, size):
    calculate_floor(k)

#print(max_tower)

print(max(max_tower[size-1]))
