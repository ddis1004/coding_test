colors = list(map(int, input().split()))

#no using extra color array

index_0 = 0
index_1 = len(colors) - 1
index_2 = len(colors) - 1

def swap(idx1, idx2):
    c = colors[idx1]
    colors[idx1] = colors[idx2]
    colors[idx2] = c


for i, c in enumerate(colors):
    if c == 2:
        if index_2 <= i :
            break
        while colors[index_2] == 2:
            index_2 -= 1
        swap(i, index_2)
        index_2 -= 1

index_1 = index_2 - 1
for i in range(0, index_2, 1):
    print(i)
    if index_1 <= i:
        break
    while colors[index_1] == 1:
        index_1 -= 1
    swap(i, index_1)
    index_1 -= 1

print(colors)