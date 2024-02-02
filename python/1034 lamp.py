R, C = map(int, input().split())

table = []

for i in range(R):
    buffer = input()
    r = []
    for idx, c in enumerate(buffer):
        #r.append(int(c))
        if c == '0':
            r.append(idx)
    table.append(r)

K = int(input())

def count_ON(table, switches):
    count =  0
    for r in table:
        if switches == r:
            count += 1
    return count

answ = 0
#for each row
for r in table:
    #check if the row can be onned
    if K >= len(r) and K % 2 == len(r) % 2:  # odd odd // even even POSSIBLE
        # try counting
        answ = max(count_ON(table, r), answ)
    # else IMPOSSIBLE

print(answ)

# 같은곳 두번은 의미가 없다
# if K > R:
    # K = K % R
# 순서는 의미가 없다
#
# 0인 포지션을 열마다 센다
