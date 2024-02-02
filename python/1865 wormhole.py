TC = int(input())

def testcase():
    def bellman_ford(roads, start):
        distances = [10010 for i in range(N + 1)]
        #distances[start] = 0

        for _ in range(N - 1):
            for i in range(1, N + 1):
                for j in roads[i]:
                    if distances[j] > roads[i][j] + distances[i]:
                        distances[j] = roads[i][j] + distances[i]

        for i in range(1, N + 1):
            for j in roads[i]:
                if distances[j] > roads[i][j] + distances[i]:
                    return -1
        return 1


    N, M, W = map(int, input().split())

    if W == 0 :
        print("NO")
        return

    #roads = [[10010 for _ in range(N + 1)] for __ in range(N + 1)]
    roads = {}
    for i in range(1, N + 1):
        roads[i] = {}

    for _ in range(M):
        S, E, T = map(int, input().split())
        if E in roads[S]:
            roads[S][E] = min(roads[S][E], T)
        else:
            roads[S][E] = T

        if S in roads[E]:
            roads[E][S] = min(roads[E][S], T)
        else:
            roads[E][S] = T

    for _ in range(W):
        S, E, T = map(int, input().split())
        if E in roads[S]:
            roads[S][E] = min(roads[S][E], -T)
        else:
            roads[S][E] = -T

    if bellman_ford(roads, 1) < 0:
        print("YES")
        return
    print("NO")




for i in range(TC):
    testcase()