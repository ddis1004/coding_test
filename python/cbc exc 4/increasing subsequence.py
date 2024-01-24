sequence = list(map(int, input().split()))

def len_subsequence(sequence):
    dp = [1 for i in range(len(sequence))]
    for i in range(1, len(sequence), 1):
        for j in range(i):
            if sequence[i] > sequence[j]:
                print(f'comparing {i}, {j}')
                dp[i] = max(dp[i], dp[j]+ 1)
    print(dp)
    return max(dp)

print(len_subsequence(sequence))