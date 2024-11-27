N = int(input())
A = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

queue = [(plus, minus, multiply, divide, A[0], 1)]

max_answer = -1000000000
min_answer = 1000000000

while queue:
    (plus, minus, multiply, divide, cur_val, depth) = queue.pop(0)

    if depth == N:
        max_answer = max(max_answer, cur_val)
        min_answer = min(min_answer, cur_val)
    else:
        if plus > 0:
            queue.append((plus - 1, minus, multiply, divide, cur_val + A[depth], depth + 1))
        if minus > 0:
            queue.append((plus, minus - 1 , multiply, divide, cur_val - A[depth], depth + 1))
        if multiply > 0:
            queue.append((plus, minus, multiply - 1, divide, cur_val * A[depth], depth + 1))
        if divide > 0:
            if cur_val > 0:
                queue.append((plus, minus, multiply, divide - 1, int(cur_val / A[depth]), depth + 1))
            else :
                queue.append((plus, minus, multiply, divide - 1, -int( abs(cur_val) / A[depth]), depth + 1))


print(max_answer)
print(min_answer)

