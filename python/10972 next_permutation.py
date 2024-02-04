N = input()
permutation = list(map(int, input().split()))


def next_permutation(p):
    length = len(p)
    swap_point = length - 1

    # find the swap point
    while swap_point != 0 and p[swap_point] <= p[swap_point - 1]:
        swap_point -= 1
    swap_point -= 1

    # if the order is in reverse, just return The End
    if swap_point == -1:
        print(-1)
        return

    swap_point2 = swap_point + 1
    for i in range(swap_point2, length):
        if p[swap_point] < p[i] and p[swap_point2] > p[i]:
            swap_point2 = i

    p[swap_point], p[swap_point2] = p[swap_point2], p[swap_point]

    p[swap_point + 1:] = sorted(p[swap_point + 1:])

    print(*p)

next_permutation(permutation)