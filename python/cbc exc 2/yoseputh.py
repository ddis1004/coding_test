N, K = map(int, input().split())
circle = list(range(1, N + 1, 1))

#print(circle)
order =[]

cursor = -1
def out(circle):
    global cursor
    cursor += K
    cursor %= len(circle)
    c = circle.pop(cursor)
    cursor -= 1
    return c

def _print(order):
    print('<', end ="")
    for i in range(N-1):
        print(f'{order[i]}, ', end="")
    print(f'{order.pop()}>', end="")

while len(circle):
    order.append(out(circle))

_print(order)