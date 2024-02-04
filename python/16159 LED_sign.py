def next_permutation(p):
    length = len(p)
    swap_point = length - 1

    # find the swap point
    while swap_point != 0 and p[swap_point] <= p[swap_point - 1]:
        swap_point -= 1
    swap_point -= 1

    # if the order is in reverse, just return The End
    if swap_point == -1:
        return -1

    swap_point2 = swap_point + 1
    for i in range(swap_point2, length):
        if p[swap_point] < p[i] and p[swap_point2] > p[i]:
            swap_point2 = i

    p[swap_point], p[swap_point2] = p[swap_point2], p[swap_point]

    p[swap_point + 1:] = sorted(p[swap_point + 1:])

    return p

row = input()
length = len(row) // 6
one_counts = [0 for i in range(length)]

for i in range(7):
    for idx, c in enumerate(row):
        if c == '1':
            one_counts[idx // 6] += 1
    if i != 6:
        row = input()

one_count_dictionary = {10: 0,
                        6: 1,
                        14: 2,
                        9: 3,
                        11: 4,
                        13: 5,
                        12: 6,
                        8: 7,
                        16: 8,
                        15: 9}
permutation = []

for count in one_counts:
    permutation.append(one_count_dictionary[count])

answ = next_permutation(permutation)

print_dict = {
    0: ["000000", "001100", "010010", "010010", "010010", "001100", "000000"],
    1: ["000000", "000100", "001100", "000100", "000100", "000100", "000000"],#
    2: ["000000", "011110", "000010", "011110", "010000", "011110", "000000"],#
    3: ["000000", "011100", "000010", "000100", "000010", "011100", "000000"],
    4: ["000000", "000100", "001100", "010100", "111110", "000100", "000000"],#
    5: ["000000", "011110", "010000", "011100", "000010", "010010", "001100"],
    6: ["000000", "010000", "010000", "011110", "010010", "011110", "000000"],
    7: ["000000", "011110", "000010", "000100", "000100", "000100", "000000"],
    8: ["000000", "011110", "010010", "011110", "010010", "011110", "000000"],
    9: ["011110", "010010", "010010", "011110", "000010", "000010", "000010"]
}

if answ == -1:
    print("The End")
else:
    #print(answ)
    for i in range(7):
        for n in answ:
            print(print_dict[n][i], end="")
        print("")