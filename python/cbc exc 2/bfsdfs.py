N, M, V = map(int, input().split())

graph = [[] for i in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)
    graph[y - 1].append(x - 1)

for i in range(N):
    graph[i] = sorted(graph[i])

def dfs(graph):
    check = [0 for i in range(N)]
    stack = []

    stack.append(V-1)
    while len(stack) > 0: #until all nodes are visited
        node = stack.pop()
        if check[node] == 1:
            continue
        print(node + 1, end=" ")
        check[node] = 1

        for i in range(len(graph[node]) - 1, -1, -1):
            if check[graph[node][i]] == 0:
                stack.append(graph[node][i])

    return


def bfs(graph):
    check = [0 for i in range(N)]
    queue = []

    queue.append(V - 1)
    check[V - 1] = 1

    while len(queue) > 0:
        node = queue.pop(0)
        print(node + 1, end=" ")
        for i in range(len(graph[node])):
            if check[graph[node][i]] == 0:
                queue.append(graph[node][i])
                check[graph[node][i]] = 1


dfs(graph)
print()
bfs(graph)

