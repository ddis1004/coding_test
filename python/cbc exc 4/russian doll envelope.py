envelopes1 = [[5,4], [2,4], [6,4], [6,7], [2,3]]

sorted_envelope = sorted(envelopes1)


def is_bigger(inner, outer):
    if inner[0] < outer[0] and inner[1] < outer[1]:
        return True
    else:
        return False

dp = [1]

def lis(idx, envelopes):
    possible_answer = 0
    for i in range(idx, -1, -1):
        print(i)
        if is_bigger(envelopes[i], envelopes[idx]):
            possible_answer = max(possible_answer, dp[i] + 1)
    return possible_answer

for i in range(1, len(sorted_envelope), 1):
    dp.append(lis(i, sorted_envelope))

print(dp)