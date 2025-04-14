from collections import defaultdict
r, c, k = map(int, input().split())
array = [list(map(int,  input().split())) for i in range(3)]

answ = -1
for i in range(101):
    new_array = []
    if r-1 < len(array) and c-1 < len(array[0]) and array[r-1][c-1] == k:
        answ = i
        break
        
    row_count = len(array)
    col_count = len(array[0])
    
    if row_count >= col_count : # do R
        max_length = 0
        for i in range(row_count):
            counts = defaultdict(int)
            for j in range(col_count):
                if not array[i][j] == 0:
                    counts[array[i][j]] += 1
            sorted_item = sorted(counts.items(), key=lambda pos:(pos[1], pos[0]))
            max_length = max(len(sorted_item) * 2, max_length)
            row = []
            for item in sorted_item:
                row.append(item[0])
                row.append(item[1])
            new_array.append(row)
        for i in range(row_count):
            for _ in range(max_length - len(new_array[i])):
                new_array[i].append(0)
    else:
        max_length = 0
        for j in range(col_count):
            counts = defaultdict(int)
            for i in range(row_count):
                if not array[i][j] == 0:
                    counts[array[i][j]] += 1
            sorted_item = sorted(counts.items(), key=lambda pos:(pos[1], pos[0]))
            max_length = max(len(sorted_item) * 2, max_length)
            col = []
            for item in sorted_item:
                col.append(item[0])
                col.append(item[1])
            new_array.append(col)
        for i in range(len(new_array)):
            for _ in range(max_length - len(new_array[i])):
                new_array[i].append(0)
        new_array = list(map(list, zip(*new_array)))
    array = new_array

print(answ)