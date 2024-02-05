x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

vec1 = (x1 - x2, y1 - y2)
vec2 = (x3 - x2, y3 - y2)

det = vec1[0] * vec2[1] - vec1[1] * vec2[0]

if det == 0:
    print(0)
elif det < 0:
    print(1)
elif det > 0:
    print(-1)

