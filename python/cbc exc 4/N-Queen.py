Q, N  = map(int, input().split())

def is_safe(x,y, queen_locations):
    for q in queen_locations:
        if x == q[0]:
            return False
        if y == q[1]:
            return False
        if abs(x - q[0]) == abs(y - q[1]):
            return False
        if x == q[0] and y == q[1]:
            return False
    return True

answer_count = 0
answer = []

def place_a_queen(current_count, queen_location):
    #print(current_count, queen_location)
    global answer_count
    if answer_count == 1:
        return True
    if current_count == Q:
        #print('all placed')
        print(queen_location)
        answer_count = 1
        queen_location.pop()
        return True

    unsafe_count = 0
    for i in range(N):
        for j in range(N):
            if is_safe(i, j, queen_location):
                #print(f'{i},{j} looks safe')
                queen_location.append((i, j))
                if not place_a_queen(current_count + 1, queen_location):
                    #print(f'{i},{j} was not safe backtracking')
                    queen_location.pop()
                    unsafe_count += 1
                else:
                    return
            else:
                unsafe_count += 1

    if unsafe_count == N*N:
        return False

place_a_queen(0, [])
print(answer)