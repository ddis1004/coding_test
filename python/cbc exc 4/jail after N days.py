initial_jail = list(map(int, input().split()))

N = 7

def next_day(initial_jail):
    answer = [0 for i in range(8)]
    for i in range(1, 7, 1):
        left = initial_jail[i - 1]
        right = initial_jail[i + 1]
        if left == right:
            answer[i] = 1
    return answer

for i in range(N):
    initial_jail = next_day(initial_jail)
    print(initial_jail)
