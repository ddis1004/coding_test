m, n = map(int, input().split())

input_list = list(map(int, input().split()))
queen_loc = [input_list[x:x+2] for x in range(1, len(input_list), 2)]
input_list = list(map(int, input().split()))
knight_loc = [input_list[x:x+2] for x in range(1, len(input_list), 2)]
input_list = list(map(int, input().split()))
pawn_loc = [input_list[x:x+2] for x in range(1, len(input_list), 2)]
del input_list

def queen_safe(x, y):
    for qloc in queen_loc:
        obstacle_count = 0
        if qloc[0] == x:        #가로
            if qloc[1] == y: #퀸과 위치가 같다면 False
                return False
            obstacle_count = 0
            for kloc in knight_loc:
                if kloc[0] == x and kloc[1] in range(y, qloc[1]): #중간에 장애물이 있으면 안전
                    obstacle_count += 1
            for ploc in pawn_loc:
                if ploc[0] == x and ploc[1] in range(y, qloc[1]): #중간에 장애물이 있으면 안전
                    obstacle_count += 1
            if obstacle_count == 0:
                return False
        elif qloc[1] == y:              #세로
            obstacle_count = 0
            for kloc in knight_loc:
                if kloc[1] == y and kloc[0] in range(x, qloc[0]): #중간에 장애물이 있으면 안전
                    obstacle_count += 1
            for ploc in pawn_loc:
                if ploc[1] == y and ploc[0] in range(x, qloc[0]): #중간에 장애물이 있으면 안전
                    obstacle_count += 1
            if obstacle_count == 0:
                return False
        elif abs(x - qloc[0]) == abs(y - qloc[1]):
            for kloc in knight_loc: # 장애물체크
                if abs(kloc[0] - qloc[0]) == abs(kloc[1] - qloc[1]) and kloc[0] in range(min(x,qloc[0]), max(x,qloc[0])):
                    obstacle_count += 1
            for ploc in pawn_loc:
                if abs(ploc[0] - qloc[0]) == abs(ploc[1] - qloc[1]) and ploc[0] in  range(min(x,qloc[0]), max(x,qloc[0])):
                    obstacle_count += 1
            if obstacle_count == 0:
                return False
    return True


def knight_safe(x, y):
    for kloc in knight_loc:
        if kloc[0] == x and kloc[1] == y:   #나이트와 위치가 같다면 x
            return False
        if x == kloc[0] + 1:
            if y == kloc[1] + 2 or y == kloc[1] - 2:
                return False
        if x == kloc[0] - 1:
            if y == kloc[1] + 2 or y == kloc[1] - 2:
                return False
        if y == kloc[1] + 1:
            if x == kloc[0] + 2 or y == kloc[0] - 2:
                return False
        if y == kloc[1] - 1:
            if x == kloc[0] + 2 or y == kloc[0] - 2:
                return False
    return True

def pawn_safe(x,y):
    for ploc in pawn_loc:
        if ploc[0] == x and ploc[1] == y:
            return False
    return True

safe_count = 0;
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if queen_safe(i, j) and knight_safe(i, j) and pawn_safe(i,j):
            #print(
            safe_count += 1

print(safe_count)