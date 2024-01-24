N = int(input())
seg_list = []

for i in range(N):
    seg_list.append(list(map(int, input().split())))

seg_list = sorted(seg_list)
integrated = []

for i in range(N):
    if i == 0:
        integrated.append(seg_list[0])
    else:
        print(f'current integrated : {integrated}, this interval : {seg_list[i]}')
        last_interval = integrated[len(integrated) - 1]
        if last_interval[1] >= seg_list[i][0]: #when overlaps
            last_interval = [last_interval[0], max(seg_list[i][1], last_interval[1])]
            integrated[len(integrated) - 1] = last_interval
        else: #no overlaps
            integrated.append(seg_list[i])

print(integrated)