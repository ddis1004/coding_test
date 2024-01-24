initial_string = input()

counts = [[chr(ord('a') + j), 0] for j in range(26)]

for c in initial_string:
    counts[ord(c) - ord('a')][1] += 1

counts = sorted(counts, key = lambda x:x[1], reverse = True)

def create_string(counts):
    previous_char = None
    answer = []
    while not counts[0][1] == 0:
        if previous_char == counts[0][0]:
            answer.append(counts[1][0])
            previous_char = counts[1][0]
            counts[0][1] -= 1
        else:
            answer.append(counts[0][0])
            previous_char = counts[0][0]
            counts[0][1] -= 1
        counts = sorted(counts, key = lambda x:x[1], reverse = True)
    return answer


if counts[0][1] > int((len(initial_string) + 1)/2):
    print(False)
else:
    print(create_string(counts))
