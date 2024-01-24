import copy

n = int(input())
num_list = list(map(int, input().split()))
max_count = int(input())

def check(x):
    possible = 0
    if x == 0:
        possibility = [[0 for i in range(n)]]
        previous_answ[0] = possibility
        return True
    else:
        #check previous answ from highest
        previous_answ.append([])
        for i in range(n):
            if num_list[i] > x:
                break;
            for pp in previous_answ[x-num_list[i]]:
                if sum(pp) < max_count:
                    answ = copy.deepcopy(pp)
                    answ[i] += 1
                    if not answ in previous_answ[x]:
                        previous_answ[x].append(answ)
                        possible += 1
    if possible > 0:
        return True
    else:
        return False


initial_num_left = [max_count for i in range(n)]
previous_answ = [[[]]]

i = 0
while check(i):
    i += 1

if i % 2 == 0:
    print(f"holsoon win at {i}")
else:
    print(f"jjaksoon win at {i}")
