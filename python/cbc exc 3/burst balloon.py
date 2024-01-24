balloons = list(map(int, input().split()))
balloons.insert(0, 1)
balloons.append(1)
N = len(balloons)

dp = [[0 for i in range(N)] for j in range(N)]

def dynamic_shit(i, j):
    if j-i == 2: # 3개 구간
        dp[i][j] = balloons[i] * balloons[j] * balloons[i+1]
    elif j-i == 3: # 4개 구간
        first_shit = balloons[i+1] * balloons[i] * balloons[i+2] + balloons[i+2] * balloons[i] * balloons[j]
        second_shit = balloons[i+2] * balloons[i+1] * balloons[j] + balloons[i+1] * balloons[i] * balloons[j]
        print(first_shit, second_shit)
        maximum_shit = max(first_shit, second_shit)
        dp[i][j] = maximum_shit

    elif j - i < 2:
        return
    else: # 5 or more
        maximum = 0
        for k in range(i + 1, j, 1):
            maximum = max(dp[i][k] + dp[k][j] + balloons[k] * balloons[i] * balloons[j], maximum)
            print(f'i : {i}, j: {j}, k: {k}, value: {dp[i][k] + dp[k][j] + balloons[k] * balloons[i] * balloons[j]}')
        dp[i][j] = maximum
    print(f'length: {j - i} i: {i} j: {j}, dp[i][j] : {dp[i][j]}')

for length in range(3, N + 1, 1):
    for i in range(0, N - length + 1, 1):
        dynamic_shit(i, i + length-1)

print(dp)
print(dp[0][5])


