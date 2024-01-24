from itertools import permutations
import math
N, SUM = map(int, input().split())

sequence_queue = []
coef_list = []

def seq_create(num_left):
    if len(num_left) == 1:
        return [num_left[0]]
    else:
        for idx, i in enumerate(num_left):
            num_left.pop(idx)
            seq = seq_create(num_left)
            seq.insert(0, i)
            num_left.insert(idx, i)
            if len(num_left) == N:
                sequence_queue.append(seq)
            else:
                return seq

def sumTriangle(n, array):
    sum = 0
    for i in range(n):
        sum += array[i]*coef_list[i]
    return sum


def getCoefList(n):
    answ = []
    coef = 1

    for i in range(int(n / 2) + 1):
        answ.append(coef)
        coef = int(coef * (n - i) / (i + 1))

    if n % 2: # when n i s odd
        answ.append(coef)
        coef = int(coef * (n - i) / (i + 1))

    for i in range(int(n / 2)):
        answ.append(int(answ[int(n / 2) - i - 1]))

    return answ


onetonlist = [*range(1, N + 1, 1)]
permute = permutations(onetonlist, N)
coef_list= getCoefList(N-1)

for p in permute:
    if sumTriangle(N, p) == SUM:
        for i in p:
            print(i, end=" ")
        break








