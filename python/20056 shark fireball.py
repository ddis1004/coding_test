from heapq import heappop, heappush
N, M, K = map(int, input().split())
fireballs = []
for i in range(M):
    fireballs.heappush(tuple(map(int, input().split())))
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def divide():
    pass

for i in range(K):
    same_loc_count = 0
    all_same_direction = True
    mass_sum = 0
    new_fireballs = []
    while(fireballs):
        r, c, m, d_1, s = fireballs.heappop()
        mass_sum += m
        same_loc_count += 1
        
        while fireballs and r == fireballs[0][0] and c == fireballs[0][1]:
            r, c, m, d_2, s = fireballs.heappop()
            mass_sum += m
            same_loc_count += 1
            
        
        divide()