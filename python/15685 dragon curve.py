N = int(input())

dragon_curves = [tuple(map(int, input().split())) for _ in range(N)] 
#(x, y, d, g) = (start_x, start_y, direction, generation)
grid = [[False for i in range(100)] for j in range(100)]
max_gen = max(g for _, _, _, g in dragon_curves)

pre_calculated_dragon = {}

def clockwise(points, time = 1):
    time = time % 4  
    if time == 0:
        return points
    elif time == 1:
        return [(-p[1], p[0]) for p in points]
    elif time == 2:
        return [(-p[0], -p[1]) for p in points]
    elif time == 3:
        return [(p[1], -p[0]) for p in points]
            
def dragon_curve(g):
    """
    g세대 드래곤 커브를 생성하는 함수.
    """
    if g == 0:
        if g not in pre_calculated_dragon.keys():
            pre_calculated_dragon[g] = [(0, 0), (1, 0)]
        return [(0, 0), (1, 0)]  # 0세대 드래곤 커브
    else:
        prev_curve = dragon_curve(g - 1)
        end_point = prev_curve[-1]
        trimmed = prev_curve[0: len(prev_curve) - 1]        
        moved = [(x - end_point[0], y - end_point[1]) for (x, y) in trimmed]
        rotated = clockwise(moved)
        append_curve = [(x + end_point[0], y + end_point[1]) for (x, y) in rotated]
        new_curve = prev_curve + list(reversed(append_curve))

        if g not in pre_calculated_dragon.keys():
            pre_calculated_dragon[g] = new_curve
        return new_curve

    
dragon_curve(max_gen)
curves = []

for c in dragon_curves:
    x_start, y_start, d, g = c 
    points = [(x_start + x, y + y_start)for (x, y) in clockwise(pre_calculated_dragon[g], d)]
    curves.append(points)

for curve in curves:
    for x, y in curve:
        grid[x][y] = True

count = 0
for x in range(99):
    for y in range(99):
        if grid[x][y] and grid[x+1][y] and grid[x][y+1] and grid[x+1][y+1]:
            count += 1

print(count)
