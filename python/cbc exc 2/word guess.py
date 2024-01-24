from itertools import permutations
N = int(input())
words = []
for i in range(N):
    words.append(list(input()))

stack = []

def next_word(w):
    buffer_queue = []
    is_swapped = False
    for i in range(len(w)-1, -1, -1):
        if w[i] > w[i-1]: #time for swap
            is_swapped = True
            #print(f'found swap point at {i}, w[i] : {w[i]}, w[i-1]: {w[i-1]}')
            buffer_queue.append(w.pop())
            temp = w[i-1]
            for idx, b in enumerate(buffer_queue):
                if b > w[i-1]:
                    w[i-1] = b
                    buffer_queue[idx] = temp
                    break
            #print(f'w : {w} , buffer_queue: {buffer_queue}')
            w += buffer_queue
            break
        else:
            buffer_queue.append(w.pop())

    if is_swapped:
        return w
    else:
        buffer_queue.reverse()
        return buffer_queue

for w in words:
    print("".join(next_word(w)))